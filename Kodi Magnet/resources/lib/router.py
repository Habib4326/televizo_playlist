import sys
from urllib.parse import parse_qsl

# ui থেকে শুধু মেনু ফাংশনগুলো নিন এবং player থেকে play_item নিন
from resources.lib.ui import home_menu, list_items
from resources.lib.player import play_item

def run_router():

    params = dict(parse_qsl(sys.argv[2][1:])) if len(sys.argv) > 2 else {}

    action = params.get("action")

    if action == "play":
        play_item(params.get("url"))
    elif action == "list":
        list_items(params.get("cat"))
    else:
        home_menu()