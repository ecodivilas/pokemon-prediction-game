from PIL import Image, ImageTk
from io import BytesIO
import requests

def get_pokemon_png(poke_name):
    URL = f"https://courses.cs.washington.edu/courses/cse154/webservices/pokedex/sprites/{poke_name}.png"
    # Sending get request and saving the response as response object
    res = requests.get(url = URL)

    # print(res) # 200 OK success
    if res.status_code == 200:
            raw_data = res.content
            im = Image.open(BytesIO(raw_data))
            return ImageTk.PhotoImage(im)
            
    # print(res) # 400 Error failed
    else:
        pass    # print(res.status_code) # Comment-out to avoid unnecessary printing