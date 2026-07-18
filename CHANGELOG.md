# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.2.2] - 2026-07-18

### 🔧 Fixes & Improvements
- Identify this repository as an unofficial community fork of dreo-team/hass-dreoverse: update `hacs.json` display name, `manifest.json` name/documentation/issue_tracker/codeowners, README, and issue template links to point at this fork instead of the upstream repo

## [2.2.1] - 2026-02-24

### 🔧 Fixes & Improvements
- Add `issue_tracker` in manifest for HACS validation
- Enforce full HACS validation (no brands ignore)

## [2.2.0] - 2026-01-27

### ✨ Features
- Add configurable oscillation angle for oscillating fans

### 🔧 Fixes & Improvements
- Fix thermostat temperature unit display issue
- Reduce control latency for more responsive device commands
- Optimize internal code paths for stability and readability

## [2.1.4] - 2025-10-09

### 🔧 Fixes & Improvements
- Fix temperature unit for heater devices
- Add device initialization status

## [2.1.3] - 2025-09-30

### ✨ Features
- Add device support: Space Heaters (HSH)

### 🔧 Fixes & Improvements
- Optimize entity generation logic for common entities

## [2.1.2] - 2025-09-28

### 🔧 Fixes
- FIx hec002 device can't control bug

## [2.1.1] - 2025-09-26

### 🔧 Fixes
- Fix inability to control humidifier display (screen)
- Fix HDH (Dehumidifier) devices failing to load

## [2.1.0] - 2025-09-25

### ✨ Features
- Add device support: HHM (Humidifiers), HDH (Dehumidifiers), HEC (Evaporative Coolers), HAC (Air Conditioners), Circulator (HAF/HPF), Ceiling Fans (HCF)
- pydreo-cloud: add `version` parameter to all API requests

### 🔧 Fixes & Improvements
- Various bug fixes and code optimizations

## [2.0.1] - 2025-08-26

### 🔄 Dependency Update
- Bump `pydreo-cloud` to `0.0.7`

### 🌍 Regional & Authentication
- European Region Support: Added support for European region user login
- Smart Region Detection: Automatically select the correct API server based on user token
- Automatic detection of token suffix (EU/NA) to determine API endpoint
- Support for token format: `token:EU` (European region) and `token:NA` (North American region)
- Tokens without suffix default to the North American endpoint

### ✅ Backward Compatibility
- Maintain full compatibility with existing North American users; no changes required

## [2.0.0] - 2025-07-13

### 🚀 Major Updates

#### Architecture Improvements
- **Core Architecture Refactoring**: Comprehensive optimization of the underlying `pydreo` package, enhancing overall performance and stability
- **Dependency Management Optimization**: Updated `pydreo-cloud` dependency package to ensure better compatibility and feature support
- **Communication Protocol Enhancement**: Optimized communication mechanism with Dreo cloud services, improving response speed and reliability

#### Code Optimization
- **Code Refactoring**: Comprehensive code optimization to improve code quality and maintainability
- **Performance Enhancement**: Optimized device state update mechanism to reduce unnecessary API calls
- **Error Handling**: Enhanced exception handling logic to improve system stability and user experience

### 🆕 New Device Support

#### Tower Fans
 **511S/611S (DR-HAF001S)**: 4-speed control, preset modes, oscillation
- **PolyFan S (DR-HAF003S)**: 8-speed control, multi-direction oscillation
- **714S/814S (DR-HAF004S)**: 9-speed control, pan-tilt oscillation
- **Falcon S (DR-HPF001S)**: 8-speed control, basic oscillation
- **Falcon X (DR-HPF002S)**: 8-speed control, directional oscillation
- **CF714S (DR-HPF004S)**: 9-speed control, directional oscillation
- **PolyFan Pro S (DR-HPF005S)**: 10-speed control, directional oscillation
- **PF707S (DR-HPF007S)**: 10-speed control, smart follow mode
- **PolyFan 508S (DR-HPF008S)**: 9-speed control, ambient lighting
- **Falcon X (DR-HPF010S)**: 8-speed control, directional oscillation

#### TurboPoly™ Fans
- **TurboPoly™ Table Fan 511S (DR-HAF001S)**: 4-speed control, preset modes, oscillation
- **TurboPoly™ Fan 513S (DR-HAF003S)**: 8-speed control, multi-direction oscillation
- **TurboPoly™ Table Fan 714S (DR-HAF004S)**: 9-speed control, pan-tilt oscillation
- **TurboPoly™ Fan 311S (DR-HPF001S)**: 8-speed control, basic oscillation
- **TurboPoly™ Fan 502S (DR-HPF002S)**: 8-speed control, directional oscillation
- **TurboPoly™ Fan 704S (DR-HPF004S)**: 9-speed control, directional oscillation
- **TurboPoly™ Fan 715S (DR-HPF005S)**: 10-speed control, directional oscillation
- **TurboPoly™ Fan 707S (DR-HPF007S)**: 10-speed control, smart follow mode
- **TurboPoly™ Fan 508S (DR-HPF008S)**: 9-speed control, ambient lighting
- **TurboPoly™ Fan 765S (DR-HPF010S)**: 8-speed control, directional oscillation

#### Air Conditioners
- **Portable Air Conditioner 516S (DR-HAC006S)**: Complete climate control with temperature (64-86°F), humidity (40-70%), multiple HVAC modes (Cool/Dry/Fan Only)

#### Ceiling Fans
- **Ceiling Fan 513S (DR-HCF003S)**: 12-speed fan control, integrated lighting with brightness and color temperature adjustment

#### Humidifiers
- **Evaporative Cooler 712S (DR-HEC002S)**: Humidity control (40-90%), oscillation, multiple operating modes (Normal/Auto/Sleep/Natural)

### 🔧 Technical Improvements

#### Enhanced Features
- **Device Discovery**: Improved automatic device discovery mechanism to support automatic recognition of more device types
- **State Synchronization**: Optimized device state synchronization logic to ensure consistency between Home Assistant and actual devices
- **Configuration Process**: Simplified device configuration process to improve user experience

#### Bug Fixes
- Fixed connection issues for certain devices during network instability
- Resolved device state update delays
- Fixed device model identification errors for some models

### 🛠️ Breaking Changes
- This version includes major architectural adjustments - users are advised to backup configurations before upgrading
- Some legacy configurations may need to be reconfigured

### 📋 Compatibility
- Supports Home Assistant 2024.12.0 and above
- Requires Python 3.11 or higher
- Compatible with HACS installation

### 🙏 Acknowledgments
Special thanks to community users for their feedback and testing, particularly those who provided device testing and debugging support.

---

## [1.0.0] - 2024-XX-XX

### 🚀 Initial Release
- Initial release of Dreo smart device Home Assistant integration
- Support for basic tower fan device control functions
- Provides device discovery and configuration functionality 
