import xbmcplugin
import xbmcgui
import sys
import urllib.parse

# নতুন ফাংশন ইম্পোর্ট করুন
from resources.lib.data import get_movies

addon_handle = int(sys.argv[1])

def home_menu():
    items = ["Movies", "Torrent"]

    for i in items:
        li = xbmcgui.ListItem(label=i)
        
        # ক্যাটাগরি পাস করার জন্য URL টি সঠিকভাবে গঠন করা
        url = f"plugin://plugin.video.KodiMagnet?action=list&cat={urllib.parse.quote(i)}"

        xbmcplugin.addDirectoryItem(
            addon_handle,
            url,
            li,
            isFolder=True
        )

    xbmcplugin.endOfDirectory(addon_handle)


def list_items(cat):
    # সব মুভি বা টরেন্ট ডাটা ফেচ করুন
    all_items = get_movies()

    for m in all_items:
        # শুধুমাত্র ক্যাটাগরি মিললে আইটেম যোগ করুন
        if m['category'] == cat:
            url = f"plugin://plugin.video.KodiMagnet?action=play&url={urllib.parse.quote(m['magnet'])}"

            li = xbmcgui.ListItem(label=m["title"])
            
            # ইমেজ সেট করা (আপনার XML এ 'image' ট্যাগ আছে তাই এটি ব্যবহার করছি)
            li.setArt({'icon': m['image'], 'fanart': m['image']})
            
            li.setInfo("video", {"title": m["title"]})
            li.setProperty('IsPlayable', 'true')

            xbmcplugin.addDirectoryItem(
                addon_handle,
                url,
                li,
                isFolder=False
            )

    xbmcplugin.endOfDirectory(addon_handle)