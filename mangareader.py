import re
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
       

if __name__ == "__main__":

    urllist = []
    namelist = []
    i = 0
    url = raw_input("Enter the link to the manga\n")

    link_pattern = re.compile(r'mangareader.net/(.*?)/(\d+)/')
    result = re.match(link_pattern, url)
    mangaName = result.group(1)
    mangaChapter = result.group(2)

    while True:

        i += 1
        url_now = 'http://www.mangareader.net/' + mangaName + '/' + mangaChapter + '/' + str(i)
        content = get_page(url_now)
        content = content.replace("\n", '')

        content_pattern = re.compile(r"document\['pu'\]\s=\s'(.*?)';")
        result = re.findall(content_pattern, content)

        if len(result) == 0:
            break

        k = len(result[0]) - 1
        if k == -1:
            break

        urllist.append(result[0])

        while result[0][k] != '/':
            k -= 1

        S = ""

        for p in xrange(k+1, len(result[0])):
            S += result[0][p]

        namelist.append(S)

    for i in xrange(0, len(urllist)):
        download(urllist[i], namelist[i])
