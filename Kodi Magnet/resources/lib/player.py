import xbmc
import xbmcgui
import urllib.parse

def play_item(magnet):

    if not magnet:
        xbmcgui.Dialog().notification("Error", "No URL")
        return

    encoded = urllib.parse.quote(magnet, safe='')
    url = f"plugin://plugin.video.elementum/play?uri={encoded}"

    xbmc.Player().play(url)