"""Config flow to configure Dreo."""

from __future__ import annotations

import hashlib
from typing import TYPE_CHECKING, Any

import voluptuous as vol
from homeassistant.config_entries import (
    ConfigEntry,
    ConfigEntryState,
    ConfigFlow,
    ConfigFlowResult,
    OptionsFlow,
)
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME
from homeassistant.core import callback
from homeassistant.helpers import selector
from pydreo.client import DreoClient
from pydreo.exceptions import DreoBusinessException, DreoException

if TYPE_CHECKING:
    from . import DreoConfigEntry

from .const import (
    CONF_EXTERNAL_TEMP_ENABLED,
    CONF_EXTERNAL_TEMP_SENSORS,
    DOMAIN,
    DreoDeviceType,
)

DATA_SCHEMA = vol.Schema(
    {vol.Required(CONF_USERNAME): str, vol.Required(CONF_PASSWORD): str}
)


class DreoFlowHandler(ConfigFlow, domain=DOMAIN):
    """Handle a Dreo config flow."""

    VERSION = 1

    @staticmethod
    @callback
    def async_get_options_flow(
        _config_entry: ConfigEntry,
    ) -> DreoOptionsFlowHandler:
        """Get the options flow for this handler."""
        return DreoOptionsFlowHandler()

    @staticmethod
    def _hash_password(password: str) -> str:
        """Hash password using MD5 (API requirement)."""
        return hashlib.md5(password.encode("UTF-8")).hexdigest()  # noqa: S324

    async def _validate_login(
        self, username: str, password: str
    ) -> tuple[bool, str | None]:
        """Validate login credentials."""
        client = DreoClient(username, password)

        try:
            await self.hass.async_add_executor_job(client.login)
        except DreoException:
            return False, "cannot_connect"
        except DreoBusinessException:
            return False, "invalid_auth"
        return True, None

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle a flow initialized by the user."""
        errors: dict[str, str] = {}
        if user_input:
            username = user_input[CONF_USERNAME]
            hashed_password = self._hash_password(user_input[CONF_PASSWORD])

            await self.async_set_unique_id(username.lower())
            self._abort_if_unique_id_configured()

            is_valid, error = await self._validate_login(username, hashed_password)
            if is_valid:
                return self.async_create_entry(
                    title=username,
                    data={CONF_USERNAME: username, CONF_PASSWORD: hashed_password},
                )
            errors["base"] = error if error else "unknown_error"
        return self.async_show_form(
            step_id="user", data_schema=DATA_SCHEMA, errors=errors
        )


class DreoOptionsFlowHandler(OptionsFlow):
    """Handle Dreo options: external temperature sensors for AC devices."""

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Manage the external temperature sensor mapping for AC devices."""
        entry: DreoConfigEntry = self.config_entry

        if entry.state is not ConfigEntryState.LOADED:
            return self.async_abort(reason="entry_not_loaded")

        hac_devices = [
            device
            for device in entry.runtime_data.devices
            if device.get("deviceType") == DreoDeviceType.HAC and device.get("deviceSn")
        ]
        if not hac_devices:
            return self.async_abort(reason="no_hac_devices")

        current_sensors = entry.options.get(CONF_EXTERNAL_TEMP_SENSORS, {})

        if user_input is not None:
            new_sensors: dict[str, str] = {}
            for device in hac_devices:
                device_sn = device["deviceSn"]
                if entity_id := user_input.get(device_sn):
                    new_sensors[device_sn] = entity_id

            current_enabled = entry.options.get(CONF_EXTERNAL_TEMP_ENABLED, {})
            new_enabled = {
                device_sn: enabled
                for device_sn, enabled in current_enabled.items()
                if device_sn in new_sensors
            }

            return self.async_create_entry(
                title="",
                data={
                    CONF_EXTERNAL_TEMP_SENSORS: new_sensors,
                    CONF_EXTERNAL_TEMP_ENABLED: new_enabled,
                },
            )

        schema_dict: dict[Any, Any] = {}
        legend_parts: list[str] = []
        for device in hac_devices:
            device_sn = device["deviceSn"]
            device_name = device.get("deviceName") or device_sn
            legend_parts.append(f"{device_sn}: {device_name}")
            schema_dict[
                vol.Optional(
                    device_sn,
                    description={"suggested_value": current_sensors.get(device_sn)},
                )
            ] = selector.EntitySelector(
                selector.EntitySelectorConfig(
                    domain="sensor", device_class="temperature"
                )
            )

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(schema_dict),
            description_placeholders={"device_legend": ", ".join(legend_parts)},
        )
