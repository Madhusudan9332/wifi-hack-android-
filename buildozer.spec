[app]
title = WiFi Hack
package.name = wifihack
package.domain = org.example
source.dir = .
source.include_exts = py,png,kv,txt
version = 1.0
requirements = python3,kivy
icon.filename = assets/icon.png
orientation = portrait
fullscreen = 1
android.permissions = ACCESS_WIFI_STATE,CHANGE_WIFI_STATE,INTERNET

[buildozer]
log_level = 2
warn_on_root = 1

[platforms]
android.api = 31
android.minapi = 21
android.arch = armeabi-v7a

[android]
# (optional) If using NDK APIs or custom Java code
android.ndk = 25b
# (optional) If you want to run with python 3.10 support
android.ndk_api = 21
android.private_storage = True
