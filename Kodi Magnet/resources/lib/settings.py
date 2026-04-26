import xbmcaddon

addon = xbmcaddon.Addon()

def get_setting(key, default=None):
    value = addon.getSetting(key)
    return value if value else default