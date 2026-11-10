[app]
title = NetMonitor
package.name = netmonitor
package.domain = org.cyber
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 1.0.0
requirements = python3,kivy

# Важно: Запрашиваем сетевые разрешения для Android 11
android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
