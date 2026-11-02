<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/alryaz/hass-pandora-cas/master/images/header_dark.png">
  <img alt="Home Assistant + Pandora" src="https://raw.githubusercontent.com/alryaz/hass-pandora-cas/master/images/header_light.png">
</picture>

# _Pandora Car Alarm System_ and _Benish GPS_ for _Home Assistant_

> Automate Pandora™, PanDECT<sup>®</sup>, and Benish GUARD Force alarm systems
> with Home Assistant.
>
>
> 💬 **Technical support**<br>
> [![Telegram group](https://img.shields.io/endpoint?url=https%3A%2F%2Ftg.sumanjay.workers.dev%2Falryaz_ha_addons&style=for-the-badge)](https://telegram.dog/alryaz_ha_addons)
>
> 🥇 **Inspiration and original developer**<br>
> [![GitHub repository](https://img.shields.io/badge/GitHub-turbulator%2Fpandora--cas-blue?style=for-the-badge)](https://github.com/turbulator/pandora-cas)

[![My Home Assistant](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?repository=hass-pandora-cas&owner=henninghartwig&category=Integration)

Your car can also be part of your smart home. This integration lets you monitor,
control, and automate a vehicle equipped with a Pandora alarm system. After
setup, your Pandora™ and PanDECT<sup>®</sup> devices are automatically added to
_Home Assistant_.

The integration accesses the API used by the official _Pandora Connect_ app and
implements some of its features. Use the same credentials as on the Pandora
website ([pandora-on.com](https://pandora-on.com/login)) or in the
[Pandora Online / Connect / Pro](https://play.google.com/store/apps/details?id=ru.alarmtrade.pandora&hl=ru)
mobile app. For this fork's domain change and installation instructions, see
[Switching to pandora-on.com](INSTALL.md).

You can choose `pandora-on.com` (new, default) or `pro.p-on.ru` (legacy) under
**Configure → Integration options → API server**. Submit the form and select
**Save changes**. The choice applies to authentication, vehicle data, WebSockets,
and web translations for that account. It is also available during setup and
reauthentication.

The integration currently supports:

- [Device Tracker](#platform_device_tracker): Vehicle location.
- [Sensors](#platform_sensor): Temperature, speed, engine RPM, and more.
- [Binary Sensors](#platform_binary_sensor): Door, movement, and other states.
- [Switches](#platform_switch): Engine, active security, and other controls.
- [Lock](#platform_lock): Arming the alarm system.
- [Number](#platform_number): Climate control adjustments.
- [Services](#services_provided): Commands such as locking, unlocking, starting,
  and stopping the engine.

The integration has been successfully tested with these systems:

- PanDECT X-1700 BT
- PanDECT X-1900 BT
- Pandora DX-4G
- Pandora DX-4G S
- Pandora DX-4GL
- Pandora DX-90BT + NAV-10
- Pandora DX-9X LoRa + NAV-10
- Pandora DXL-4970
- Pandora DXL-5570
- Pandora NAV-08 _(beacon)_
- Pandora VX-4G GPS
- _[Report your success!](mailto:alryaz@alryaz.com?subject=Pandora%20Car%20Alarm%20System%20%D0%B4%D0%BB%D1%8F%20Home%20Assistant%20-%20%D0%9F%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%BA%D0%B0%20%D1%83%D1%81%D1%82%D1%80%D0%BE%D0%B9%D1%81%D1%82%D0%B2%D0%B0&body=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5!%0D%0A%0D%0A%D0%9F%D0%BE%D0%B4%D1%82%D0%B2%D0%B5%D1%80%D0%B6%D0%B4%D0%B0%D1%8E%2C%20%D1%87%D1%82%D0%BE%20%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D0%B5%D1%82%20%D1%81%20%D0%BC%D0%BE%D0%B8%D0%BC%20%D1%83%D1%81%D1%82%D1%80%D0%BE%D0%B9%D1%81%D1%82%D0%B2%D0%BE%D0%BC%20...!%0D%0A%0D%0A(%D0%95%D1%81%D0%BB%D0%B8%20%D1%8D%D1%82%D0%BE%20%D0%BD%D0%B5%20%D1%82%D0%B0%D0%BA%2C%20%D0%BE%D0%BF%D0%B8%D1%88%D0%B8%D1%82%D0%B5%2C%20%D0%BF%D0%BE%D0%B6%D0%B0%D0%BB%D1%83%D0%B9%D1%81%D1%82%D0%B0%2C%20%D0%92%D0%B0%D1%88%D0%B8%20%D0%BD%D0%B0%D0%B1%D0%BB%D1%8E%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%BE%20%D0%BD%D0%B5%D0%BF%D0%BE%D0%BB%D0%B0%D0%B4%D0%BA%D0%B0%D1%85))_

## Screenshots

<details>
    <summary>Dashboard with all supported entities</summary>
    <img src="https://raw.githubusercontent.com/alryaz/hass-pandora-cas/master/images/screenshot_default.png" alt="Screenshot: Dashboard with all supported entities">
</details>
<details>
    <summary>Calling a service from Developer Tools</summary>
    <img src="https://raw.githubusercontent.com/alryaz/hass-pandora-cas/master/images/screenshot_service_call.png" alt="Screenshot: Calling a service from Developer Tools">
</details>
<details>
    <summary>Device card (dark theme)</summary>
    <img src="https://raw.githubusercontent.com/alryaz/hass-pandora-cas/master/images/stack_default_dark.png" alt="Screenshot: Device card (dark theme)">
</details>
<details>
    <summary>Available tracker cursor styles</summary>
    <ul>
        <li><a href="https://github.com/alryaz/hass-pandora-cas/blob/master/custom_components/pandora_cas/cursors/arrow.svg" target="_blank"><img src="https://raw.githubusercontent.com/alryaz/hass-pandora-cas/master/custom_components/pandora_cas/cursors/arrow.svg" width="32" height="32" alt="Cursor: arrow"></a> &mdash; <em>arrow</em></li>
        <li><a href="https://github.com/alryaz/hass-pandora-cas/blob/master/custom_components/pandora_cas/cursors/bird.svg" target="_blank"><img src="https://raw.githubusercontent.com/alryaz/hass-pandora-cas/master/custom_components/pandora_cas/cursors/bird.svg" width="32" height="32" alt="Cursor: bird"></a> &mdash; <em>bird</em></li>
        <li><a href="https://github.com/alryaz/hass-pandora-cas/blob/master/custom_components/pandora_cas/cursors/car.svg" target="_blank"><img src="https://raw.githubusercontent.com/alryaz/hass-pandora-cas/master/custom_components/pandora_cas/cursors/car.svg" width="32" height="32" alt="Cursor: car"></a> &mdash; <em>car</em></li>
        <li><a href="https://github.com/alryaz/hass-pandora-cas/blob/master/custom_components/pandora_cas/cursors/helicopter.svg" target="_blank"><img src="https://raw.githubusercontent.com/alryaz/hass-pandora-cas/master/custom_components/pandora_cas/cursors/helicopter.svg" width="32" height="32" alt="Cursor: helicopter"></a> &mdash; <em>helicopter</em></li>
        <li><a href="https://github.com/alryaz/hass-pandora-cas/blob/master/custom_components/pandora_cas/cursors/moto.svg" target="_blank"><img src="https://raw.githubusercontent.com/alryaz/hass-pandora-cas/master/custom_components/pandora_cas/cursors/moto.svg" width="32" height="32" alt="Cursor: moto"></a> &mdash; <em>moto</em></li>
        <li><a href="https://github.com/alryaz/hass-pandora-cas/blob/master/custom_components/pandora_cas/cursors/pierced_heart.svg" target="_blank"><img src="https://raw.githubusercontent.com/alryaz/hass-pandora-cas/master/custom_components/pandora_cas/cursors/pierced_heart.svg" width="32" height="32" alt="Cursor: pierced_heart"></a> &mdash; <em>pierced_heart</em></li>
        <li><a href="https://github.com/alryaz/hass-pandora-cas/blob/master/custom_components/pandora_cas/cursors/plane.svg" target="_blank"><img src="https://raw.githubusercontent.com/alryaz/hass-pandora-cas/master/custom_components/pandora_cas/cursors/plane.svg" width="32" height="32" alt="Cursor: plane"></a> &mdash; <em>plane</em></li>
        <li><a href="https://github.com/alryaz/hass-pandora-cas/blob/master/custom_components/pandora_cas/cursors/quadrocopter.svg" target="_blank"><img src="https://raw.githubusercontent.com/alryaz/hass-pandora-cas/master/custom_components/pandora_cas/cursors/quadrocopter.svg" width="32" height="32" alt="Cursor: quadrocopter"></a> &mdash; <em>quadrocopter</em></li>
        <li><a href="https://github.com/alryaz/hass-pandora-cas/blob/master/custom_components/pandora_cas/cursors/rocket.svg" target="_blank"><img src="https://raw.githubusercontent.com/alryaz/hass-pandora-cas/master/custom_components/pandora_cas/cursors/rocket.svg" width="32" height="32" alt="Cursor: rocket"></a> &mdash; <em>rocket</em></li>
        <li><a href="https://github.com/alryaz/hass-pandora-cas/blob/master/custom_components/pandora_cas/cursors/truck.svg" target="_blank"><img src="https://raw.githubusercontent.com/alryaz/hass-pandora-cas/master/custom_components/pandora_cas/cursors/truck.svg" width="32" height="32" alt="Cursor: truck"></a> &mdash; <em>truck</em></li>
    </ul>
</details>

## Installation

### Home Assistant Community Store

> 🎉 **Recommended installation method.**

[![Open the repository in your Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=alryaz&repository=hass-pandora-cas&category=integration)

1. Install HACS ([official installation instructions](https://hacs.xyz/docs/installation/installation/)).
2. Add the repository to your custom repositories:
   1. Open the _HACS_ home page.
   2. Open _Integrations_.
   3. Click the three dots in the upper right corner.
   4. Select _Custom repositories_.
   5. Paste `https://github.com/alryaz/hass-pandora-cas` into the input field.
   6. Select _Integration_ from the dropdown.
   7. Click _Add_.
3. Search for `Pandora Car Alarm System` in the integrations list.
4. Install the latest version by clicking _Install_.
5. Restart _Home Assistant_.

### Manual installation

> ⚠️ **Warning:** This method is **<ins>not recommended</ins>** because keeping
> the installed integration up to date is more difficult.

1. Download the [latest stable integration archive](https://github.com/alryaz/hass-pandora-cas/releases/latest/download/pandora_cas.zip).
2. Create a `custom_components` directory inside your Home Assistant configuration
   directory if it does not already exist.
3. Create a `pandora_cas` directory inside `custom_components`.
4. Extract the downloaded archive into `pandora_cas`.
5. Restart _Home Assistant_.

## Configuration

### Using the _Integrations_ interface

Basic configuration through the _Home Assistant_ web interface is supported.
This method does not require restarting _Home Assistant_.

[![Set up the pandora_cas integration](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=pandora_cas)

<details>
  <summary>Manual steps if the button above does not work</summary>
  To open the configuration flow:
  <ol>
    <li>Go to <i>Settings</i> &#10230; <i>Integrations</i> (<code>/config/integrations</code>).</li>
    <li>Click the circular plus button in the lower right corner.</li>
    <li>Enter <b>Pandora</b> in the search field. One of the results should be <b>Pandora Car Alarm System</b>, with the corresponding brand logo.</li>
    <li>Select that result.</li>
    <li>Enter your username and password in the corresponding fields.</li>
    <li>Click <i>Submit</i> in the lower right corner. Any errors will appear in the dialog.</li>
    <li>The update should take no more than 5–10 seconds (tested on a Raspberry Pi 4). Entities with the default configuration should appear on the main dashboard when using the default Lovelace configuration.</li>
  </ol>
</details>

### Using YAML

> ⚠️ **Warning:** This method is **<ins>not recommended</ins>** because keeping
> the installed integration up to date is more difficult.

To enable the integration, add the following to `configuration.yaml`:

```yaml
# Excerpt from configuration.yaml
pandora_cas:
  # Pandora portal account
  password: !secret YOUR_PASSWORD  # required
  username: !secret YOUR_USERNAME  # required
```

The integration also supports multiple accounts:

```yaml
pandora_cas:
  # First account
  - username: !secret YOUR_USERNAME_1
    password: !secret YOUR_PASSWORD_1

    # Second account
  - username: !secret YOUR_USERNAME_2
    password: !secret YOUR_PASSWORD_2
```

### Managing entities through the interface

<a id="integration_entities_control"></a>

For all configuration methods, you can use the device page to manage enabled
entities:

1. Go to _Settings_ &#10230; _Devices_ (`/config/devices/dashboard`).
2. Find your device. Its _Integration_ column shows `Pandora Car Alarm System`.
3. Click the device row.
4. Scroll down to `+[N] hidden entities`.
5. Click that label.
6. Select one of the entities that appears.
7. In the dialog, switch _Enable entity_ to _On_.
8. Click _Update_ in the lower right corner of the dialog.

Example of a populated X-1911BT device page (click to enlarge):

[<img src="https://raw.githubusercontent.com/alryaz/hass-pandora-cas/master/images/screenshot_device_card_1.png" alt="X-1911BT device card, part 1" width="31%">](https://github.com/alryaz/hass-pandora-cas/blob/master/images/screenshot_device_card_1.png)
[<img src="https://raw.githubusercontent.com/alryaz/hass-pandora-cas/master/images/screenshot_device_card_2.png" alt="X-1911BT device card, part 2" width="31%">](https://github.com/alryaz/hass-pandora-cas/blob/master/images/screenshot_device_card_2.png)
[<img src="https://raw.githubusercontent.com/alryaz/hass-pandora-cas/master/images/screenshot_device_card_3.png" alt="X-1911BT device card, part 3" width="31%">](https://github.com/alryaz/hass-pandora-cas/blob/master/images/screenshot_device_card_3.png)

## Sensors / Switches / States

Sensor entity IDs use the vehicle's `PANDORA_ID`, while their display names use
the vehicle name from the Pandora website. Renaming the vehicle on the website
therefore does not change entity IDs, so you do not need to reconfigure your
Lovelace UI or automations.

> **Important:** When adding some entities, the integration checks whether the
> device supports the feature. To avoid surprises, consult the compatibility
> tables on the official Pandora website:
> [compatibility document](https://alarmtrade.ru/service/sravnitelnye-tablitsy-sistem-pandora-i-pandect/).

> **Warning:** The total number of available entity types will soon exceed 40.
> Less common entities are therefore disabled by default, including:
>
> - Hybrid/EV battery charging status and temperature.
> - Window position and tire pressure (TPMS) received over the CAN bus.
>
> These entities are marked with "&#9888;" in the tables below. If your vehicle
> and its alarm system support these features, enable the entities using the
> [instructions above](#integration_entities_control).

### `sensor` platform

<a id="platform_sensor"></a>

| Entity | Purpose | Notes |
|------------------------------------------------------------|----------------------------------------|----------------|
| sensor.`PANDORA_ID`_mileage | GPS mileage reported by the alarm system | km |
| sensor.`PANDORA_ID`_can_mileage | Factory odometer mileage (CAN bus) | km |
| sensor.`PANDORA_ID`_fuel | Fuel level <sup>1</sup> | % |
| sensor.`PANDORA_ID`_interior_temperature | Interior temperature | °C |
| sensor.`PANDORA_ID`_engine_temperature | Engine temperature | °C |
| sensor.`PANDORA_ID`_exterior_temperature | Exterior temperature | °C |
| sensor.`PANDORA_ID`_battery_temperature | Battery temperature | °C |
| sensor.`PANDORA_ID`_balance | SIM card balance | Account currency |
| sensor.`PANDORA_ID`_speed | Speed | km/h |
| sensor.`PANDORA_ID`_tachometer | Tachometer (engine speed) | rpm |
| sensor.`PANDORA_ID`_gsm_level | GSM signal strength | 0 ... 3 |
| sensor.`PANDORA_ID`_battery_voltage | Battery voltage | V |
| sensor.`PANDORA_ID`_last_online | Last connection | Timestamp |
| sensor.`PANDORA_ID`_last_state_update | Last state update | Timestamp |
| sensor.`PANDORA_ID`_last_settings_change | Last system settings change | Timestamp |
| sensor.`PANDORA_ID`_last_command_execution | Last command execution | Timestamp |
| &#9888;&nbsp;sensor.`PANDORA_ID`_balance_secondary | _Secondary SIM card balance_ | Account currency |
| &#9888;&nbsp;sensor.`PANDORA_ID`_can_mileage_to_empty | _Distance to empty (CAN bus)_ | km |
| &#9888;&nbsp;sensor.`PANDORA_ID`_left_front_tire_pressure | _Front left tire pressure_ | kPa _(?)_ |
| &#9888;&nbsp;sensor.`PANDORA_ID`_right_front_tire_pressure | _Front right tire pressure_ | kPa _(?)_ |
| &#9888;&nbsp;sensor.`PANDORA_ID`_left_back_tire_pressure | _Rear left tire pressure_ | kPa _(?)_ |
| &#9888;&nbsp;sensor.`PANDORA_ID`_right_back_tire_pressure | _Rear right tire pressure_ | kPa _(?)_ |
| &#9888;&nbsp;sensor.`PANDORA_ID`_reserve_tire_pressure | _Rear right tire pressure_ | kPa _(?)_ |

### `binary_sensor` platform

<a id="platform_binary_sensor"></a>

| Entity | Purpose | Notes |
|---------------------------------------------------------------|---------------------------------------------------|---------------------------|
| binary_sensor.`PANDORA_ID`_connection_state | Vehicle connection<sup>1</sup> | connected / disconnected |
| binary_sensor.`PANDORA_ID`_moving | Movement status | moving / stationary |
| binary_sensor.`PANDORA_ID`_left_front_door | Front left door | open / closed |
| binary_sensor.`PANDORA_ID`_right_front_door | Front right door | open / closed |
| binary_sensor.`PANDORA_ID`_left_back_door | Rear left door | open / closed |
| binary_sensor.`PANDORA_ID`_right_back_door | Rear right door | open / closed |
| binary_sensor.`PANDORA_ID`_trunk | Trunk | open / closed |
| binary_sensor.`PANDORA_ID`_hood | Hood | open / closed |
| binary_sensor.`PANDORA_ID`_parking | Parking mode | on / off |
| binary_sensor.`PANDORA_ID`_brakes | Brake pedal | pressed / released |
| &#9888;&nbsp;binary_sensor.`PANDORA_ID`_left_front_glass | _Front left window (driver)<sup>2</sup>_ | open / closed |
| &#9888;&nbsp;binary_sensor.`PANDORA_ID`_right_front_glass | _Front right window (passenger)<sup>2</sup>_ | open / closed |
| &#9888;&nbsp;binary_sensor.`PANDORA_ID`_left_back_glass | _Rear left window_ | open / closed |
| &#9888;&nbsp;binary_sensor.`PANDORA_ID`_right_back_glass | _Rear right window_ | open / closed |
| &#9888;&nbsp;binary_sensor.`PANDORA_ID`_ev_charging_connected | _EV battery charging_ | connected / disconnected |

<sup>1</sup> This entity contains the full set of properties received when the
vehicle state is updated and can be used in `template` expressions.<br>
<sup>2</sup> The integration has not been tested with right-hand-drive vehicles.
These sensors may be swapped by default.

### `lock` and `switch` platforms

<a id="platform_lock"></a>
<a id="platform_switch"></a>

| Entity | Purpose | Notes |
|-------------------------------------|------------------------------------------------|------------------------------|
| lock.`PANDORA_ID`_central_lock | Central locking status | unlocked / locked |
| switch.`PANDORA_ID`_active_security | Active security status | on / off |
| switch.`PANDORA_ID`_coolant_heater | Coolant heater status | on / off |
| switch.`PANDORA_ID`_engine | Engine status | running / stopped |
| switch.`PANDORA_ID`_tracking | Tracking status (GPS track) | on / off |
| switch.`PANDORA_ID`_service_mode | Service (maintenance) mode | on / off |
| switch.`PANDORA_ID`_ext_channel | Auxiliary channel <sup>3</sup> | enable / disable |
| switch.`PANDORA_ID`_status_output | Status output (for aftermarket immobilizers) | enable / disable |

<sup>3</sup> The state is not monitored.

### `button` platform

<a id="platform_button"></a>

| Entity | Purpose | Notes |
|------------------------------------------|-----------------------------------|------------|
| switch.`PANDORA_ID`_erase_errors | Clear fault codes |  |
| switch.`PANDORA_ID`_read_errors | Read fault codes |  |
| switch.`PANDORA_ID`_trigger_horn | Engine status |  |
| switch.`PANDORA_ID`_trigger_light | Tracking status (GPS track) |  |
| switch.`PANDORA_ID`_trigger_trunk | Service (maintenance) mode |  |
| switch.`PANDORA_ID`_check | Auxiliary channel <sup>3</sup> |  |
| switch.`PANDORA_ID`_additional_command_1 | Additional command No. 1 |  |
| switch.`PANDORA_ID`_additional_command_2 | Additional command No. 2 |  |

### `number` platform

<a id="platform_number"></a>

Number entities provide climate control adjustments.

### `device_tracker` platform

<a id="platform_device_tracker"></a>

A `device_tracker.pandora_PANDORA_ID` entity is created for each vehicle, where
`PANDORA_ID` is its unique ID in the Pandora system. Standard Device Tracker
features are available, including location tracking
[on a map](https://www.home-assistant.io/lovelace/map/),
[route history](https://www.home-assistant.io/blog/2020/04/08/release-108/#lovelace-map-history),
and [zone monitoring](https://www.home-assistant.io/docs/automation/trigger/#zone-trigger).

<details>
  <summary>Example map marker (color and rotation)</summary>
  <img src="https://raw.githubusercontent.com/alryaz/hass-pandora-cas/master/images/screenshot_map_marker.png" alt="Screenshot: Rotated vehicle marker on the Home Assistant map">
</details>

The entity has the following attributes:

| Parameter | Type | Description |
|-----------|:-------:|--------------------------------|
| latitude | `float` | Latitude |
| longitude | `float` | Longitude |
| device_id | `int` | Device ID |
| direction | `int` | Direction (degrees) |
| cardinal | `str` | Direction (compass point) |

## Events

<a id="events_supported"></a>

Some events observed while monitoring the vehicle do not map conveniently to
`sensor`, `binary_sensor`, or similar entities. Two internal event types provide
access to these additional events.

### `pandora_cas_event` events

This event forwards information from the Pandora system directly to Home
Assistant. The following data is available in the event:

| Parameter | Type | Description |
|----------------------|:-------------:|---------------------------------|
| device_id | `int` | Device ID |
| event_id_primary | `int` | Primary event code |
| event_id_secondary | `int` | Secondary event code |
| title_primary | `str`, `None` | Primary event title |
| title_primary | `str`, `None` | Secondary event title |
| event_type | `str` | Event type code |
| latitude | `float` | Latitude |
| longitude | `float` | Longitude |
| gsm_level | `int` | Signal strength |
| fuel | `int` | Fuel level |
| exterior_temperature | `int` | Exterior temperature |
| engine_temperature | `int` | Engine temperature |

The event type code is an English string that briefly describes the event.
The original documentation refers to the project's `api.py` file for the full
list of codes. See also the [event ID reference](DATA.md).

### `pandora_cas_command` events

Notification events are emitted for all commands. They contain the following data:

| Parameter | Type | Description |
|------------|:-----:|--------------------------------------------------------------------|
| device_id | `int` | Device ID |
| command_id | `int` | Command ID _(see below)_ |
| result | `int` | Execution result (`0` = success; any other value = error) |
| reply | `int` | Error description code (greater than zero if available) |

## Commands / Services

<a id="services_provided"></a>

The main commands for enabling and disabling features are exposed as entities,
such as `switch` and `lock`. To send commands beyond these predefined controls,
there are two ways to address the alarm system.

For a _named_ command, call a service in the form `pandora_cas.<suffix>`:

```yaml
# Named command call
- action: call-service
  service: pandora_cas.start_engine
  data:
    device_id: 1231234123
```

For a _generic_ command, the command ID (`command_id`) must be numeric:

```yaml
# Generic command call
- action: call-service
  service: pandora_cas.remote_command
  data:
    device_id: 1234141243
    command_id: 1
```

The available commands are listed below, grouped by purpose:

| ID | Suffix | Action | Notes |
|--------:|---------------------------|---------------------------------|-------------------------------------------------------------|
| **1** | `lock` | Arm | May be prohibited by the alarm unit settings |
| **2** | `unlock` | Disarm | May be prohibited by the alarm unit settings |
| **4** | `start_engine` | Start engine |  |
| **8** | `stop_engine` | Stop engine |  |
| **16** | `enable_tracking` | Enable GPS tracking | Not supported by all devices |
| **32** | `disable_tracking` | Disable GPS tracking | Not supported by all devices |
| **17** | `enable_active_security` | Enable active security | Not supported by all devices |
| **18** | `disable_active_security` | Disable active security | Not supported by all devices |
| **21** | `turn_on_coolant_heater` | Switch on coolant heater | Not supported by all devices |
| **22** | `turn_off_coolant_heater` | Switch off coolant heater | Not supported by all devices |
| **33** | `turn_on_ext_channel` | Enable auxiliary channel | Not supported by all devices |
| **34** | `turn_off_ext_channel` | Disable auxiliary channel | Not supported by all devices |
| **40** | `enable_service_mode` | Enable service mode |  |
| **41** | `disable_service_mode` | Disable service mode |  |
| **23** | `trigger_horn` | Sound horn |  |
| **24** | `trigger_light` | Flash lights |  |
| **255** | `check` | CHECK command | ? |
| **100** | `additional_command_1` | Additional command No. 1 | Configured using the alarm unit configuration tools |
| **128** | `additional_command_2` | Additional command No. 2 | Configured using the alarm unit configuration tools |
| **240** | `enable_connection` | Extend communication period | ? |
| **15** | `disable_connection` | End communication period | ? |
| **48** | `enable_status_output` | Disable status output | Requires support on the vehicle side |
| **49** | `disable_status_output` | Enable status output | Requires support on the vehicle side |

### Command examples

<a id="service_examples"></a>

A dashboard tab with an engine start button:

```yaml
  - badges: [ ]
    cards:
      - hold_action:
          action: call-service
          service: pandora_cas.start_engine
          data:
            id: 1234567890
        icon: 'mdi:fan'
        name: Start engine
        show_icon: true
        show_name: true
        tap_action:
          action: more-info
        type: button
    icon: 'mdi:car'
    panel: false
    path: honda_pilot
    title: Honda Pilot
```

An automation that enables the auxiliary channel when an event occurs and the
conditions are met. See the
[usage example](https://www.drive2.ru/l/526540176697066100/) for details.

```yaml
# Excerpt from automations.yaml
- id: switch_on_pilot_seat_heaters
  alias: Turn on seat heaters
  trigger:
    platform: state
    entity_id: binary_sensor.1234567890_engine_state
    to: 'on'
  condition:
    - condition: time
      after: 05:58:00
      before: 06:12:00
      weekday:
        - mon
        - tue
        - wed
        - thu
        - fri
  action:
    service: pandora_cas.turn_on_ext_channel
    data_template:
      id: 1234567890
```

## Creating a device card

Three configuration types are available:

- [Card](https://github.com/alryaz/hass-pandora-cas/tree/master/interface/cards):
  A graphical representation of the vehicle only.
- [Stack](https://github.com/alryaz/hass-pandora-cas/tree/master/interface/stacks):
  A card, controls, and sensors.
- [Dashboard](https://github.com/alryaz/hass-pandora-cas/tree/master/interface/dashboards):
  A map on the left and a stack on the right.

To prepare your own configuration:

1. Open the [prepared configurations directory](https://github.com/alryaz/hass-pandora-cas/tree/master/interface).
2. Choose a file with the configuration type you want.
3. Copy its contents into a text editor.
4. Replace every occurrence of `REPLACE_WITH_PANDORA_ID` with your vehicle ID
   (the `device_id` attribute on the sensors).

## Disclaimer

This software is not affiliated with or endorsed by NPO Telemetria LLC, the owner
of the Pandora trademark. Use it at your own risk. Under no circumstances is the
author liable for damage to or loss of your property, or for any harm to third
parties.

All brand and product names belong to their respective owners.
