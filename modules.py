import requests


def download(img_url, filename):
    
    downloaded_image = file(filename, "wb")

    image_on_web = requests.get(img_url)
    downloaded_image.write(image_on_web.content)
    downloaded_image.close()
    print filename + ' downloaded'


def get_page(url):
    r = requests.get(url)
    content = r.text.encode('utf-8', 'ignore')
    return content
