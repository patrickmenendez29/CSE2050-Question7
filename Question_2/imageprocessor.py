from urllib import request, error
from PIL import Image

def convert_to_gif(image_path):
    scaled_width = 200
    img = Image.open(image_path)
    percent_width = (scaled_width / float(img.size [0]))
    h_size = int((float(img.size [1]) * float(scaled_width )))
    img = img.resize (( scaled_width , h_size), Image.ANTIALIAS)
    filename = image_path.split("/")[-1]
    img.save("res.gif") # save the img as a GIF for loading in ezgraphics


def download_image(url):
    req = request.Request(url)
    try:
        response = request.urlopen(req)
        img_bytes = response.read()
        file_name = url[url.rindex("/") + 1 :]
        print(file_name)
        img_file = open(file_name,"wb")
        img_file.write(img_bytes)
    except error.URLError as e:
        print(e.reason)
    print("Image successfully downloaded")

