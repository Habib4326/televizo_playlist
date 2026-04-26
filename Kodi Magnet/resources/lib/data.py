import urllib.request
import xml.etree.ElementTree as ET

def get_movies():
    url = "https://raw.githubusercontent.com/Habib4326/televizo_playlist/main/data.xml"
    try:
        # requests এর বদলে urllib.request ব্যবহার করছি
        with urllib.request.urlopen(url, timeout=10) as response:
            content = response.read()
            
            # XML পার্স করা
            root = ET.fromstring(content)
            movies = []
            
            for movie in root.findall('movie'):
                movie_data = {
                    'title': movie.find('title').text if movie.find('title') is not None else "N/A",
                    'category': movie.find('category').text if movie.find('category') is not None else "Uncategorized",
                    'magnet': movie.find('magnet').text if movie.find('magnet') is not None else "",
                    'image': movie.find('image').text if movie.find('image') is not None else ""
                }
                movies.append(movie_data)
            return movies
            
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []