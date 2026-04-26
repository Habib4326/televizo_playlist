import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

# ANSI Color Codes
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def add_movie():
    print(f"{BLUE} +------------------------------------------------+{RESET}")
    print(f"{BLUE} |            Kodi XML Link Adder                 |{RESET}")
    print(f"{BLUE} +------------------------------------------------+{RESET}")
    
    title = input(f"{GREEN} | Title: {RESET}")
    magnet = input(f"{GREEN} | Link:  {RESET}")
    image_link = input(f"{GREEN} | Image Link: {RESET}")
    category = input(f"{GREEN} | Category (Movies/Torrent): {RESET}")
    
    print(f"{BLUE} +------------------------------------------------+{RESET}")
    
    if not title or not magnet or not image_link or not category:
        print(f"{RED} | Error: All fields are required!                |{RESET}")
        return

    # এখানে '&' কে '&amp;' এ রূপান্তর করার লজিক
    magnet_formatted = magnet.replace("&", "&amp;")

    file_path = "data.xml"
    
    try:
        # ফাইল না থাকলে নতুন তৈরি করা
        if not os.path.exists(file_path):
            root = ET.Element("movies")
            tree = ET.ElementTree(root)
        else:
            tree = ET.parse(file_path)
            root = tree.getroot()

        # ডুপ্লিকেট চেক (ম্যাগনেট লিঙ্ক দিয়ে চেক করছি)
        for movie in root.findall('movie'):
            if movie.find('magnet').text == magnet_formatted:
                print(f"{RED} | Error: This link already exists!               |{RESET}")
                return

        # নতুন মুভি যোগ করা
        new_movie = ET.SubElement(root, "movie")
        ET.SubElement(new_movie, "title").text = title
        ET.SubElement(new_movie, "category").text = category
        
        # ফরম্যাট করা ম্যাগনেট লিঙ্কটি এখানে বসছে
        ET.SubElement(new_movie, "magnet").text = magnet_formatted
        
        ET.SubElement(new_movie, "image").text = image_link

        # ফাইলটি সুন্দরভাবে (Pretty print) সেভ করা
        xml_str = ET.tostring(root, encoding='utf-8')
        pretty_xml = minidom.parseString(xml_str).toprettyxml(indent="    ")
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(pretty_xml)

        print(f"{GREEN} | Status: Success! Added to {category}.          |{RESET}")
            
    except Exception as e:
        print(f"{RED} | Error: {e}{RESET}")
    
    print(f"{BLUE} +------------------------------------------------+{RESET}")

if __name__ == "__main__":
    add_movie()