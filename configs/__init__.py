# coding=utf-8

from config_default import AppSettingsDefault

try:
    from settings_local import AppSettings
except:
    AppSettings = AppSettingsDefault


