## 2.1.0 - 2025-07-26

* 🔼 Add DLNA Server/Renderer and Bridge upmpdcli


## 2.0.0 - 2025-07-04

* 🔼 Replace ympd with myMPD


## 1.9.0 - 2025-07-03

* 🔼 Updated alpine image to `3.22`
* 🔼 Updated mpc to `0.35-r0`
* 🔼 Updated mpd to `0.24.4-r1`


## 1.8.0 - 2024-05-08

* 🔼 Updated alpine image to `3.19`
* 🔼 Updated mpc to `0.34-r0`
* 🔼 Updated mpd to `0.23.14-r1`
* 🔼 Updated ympd to `1.3.0-r12`


## 1.7.2 - 2022-08-17

* 🔨 Migrated to S6-Overlay `V3`
* 📝 Updated to new repository structure + Yaml config


## 1.7.1 - 2022-04-05

* 📝 Updated config.json and Readme


## 1.7.0 - 2021-04-02

* 🔨 Use ghcr.io/home-assistant for base images


## 1.6.0 - 2021-03-27

* 🐛 Fixed `media_folder`, `playlist_folder` options overwriting custom config. Thanks @LiJu09
* 🔨 Change how custom_config behave. Check docs. Thanks @LiJu09


## 1.5.4 - 2021-03-25

* ➕ Add `media_folder`, `playlist_folder` option. Thanks @LiJu09


## 1.5.3 - 2021-03-17

* 🐛 Specifiy own S6 entrypoint, don't rely on the base image.


## 1.5.2 - 2021-02-09

* 🔨 Migrate to new `devices` option format. Thanks @LiJu09


## 1.5.1 - 2021-01-30

* 🐛 Fixed missing permissions on startup


## 1.5.0 - 2021-01-30

* 🔼 Updated alpine image to `3.13`
* 🔼 Updated mpd to `0.22.3-r0`
* 🔨 Use Jemalloc for better memory handling


## 1.4.2 - 2020-11-11

* 🔨 Add httpd output config
* 🐛 Make debug config optional


## 1.4.1 - 2020-10-24

* ➕ Add `verbose` option


## 1.4.0 - 2020-10-20

* 🔼 Update alpine to `3.12`
* 🔼 Update mpd to `0.21.23-r0`
* 🔼 Update ympd to `1.3.0-r9`
* 🔼 Update mpc to `0.33-r2`
* 🔨 Use S6-Overlay for execution
* 🔨 Disable Avahi Discovery
* 🔨 Change audio output to Pulseaudio
* 🔨 Start mpd as `application` startup
* ➖ Removed alsa-plugins-pulse


## 1.3.2 - 2020-10-06

* ➕ Support `/media` folder


## 1.3.1 - 2020-05-26

* 🐛 Fixed startup without custom config file


## 1.3.0 - 2020-05-22

* ➕ Added `custom_config` option for own mpd configuration file.
* ➕ Added configuration docs
* 🔨 Updated Changelog to new format


## 1.2.0 - 2020-03-09

* ➕ Added `alsa-plugins-pulse` to be compatible with latest HassOS (> 3.11)


## 1.1.2 - 2020-02-09

* 🔨 Start mpd as `system` startup


## 1.1.1 - 2020-02-07

* 🔼 Update mpd to `0.21.16-r1`
* 🔼 Update ympd to `1.3.0-r8`
* 🔼 Update alpine to `3.11`
* 🔼 Update mpc to  `0.33-r0`


## 1.1.0 - 2019-12-14

* ➕ Add `volume_normalization` option to addon


## 1.0.0 - 2019-12-x

* ➕ Add MPD version `0.20.21`
* ➕ Add ympd version `1.3.0`
