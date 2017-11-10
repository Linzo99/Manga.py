Manga.py
========

A set of small python scripts to download manga from online manga reading sites like Mangastream or Mangareader just from a link.

## Usage

The script download the manga pages in the folder where the script is kept.

In linux, `cd` to the directory and run the script with `python manga.py`. When prompted, use the link to the manga chapter to download.

In windows, run the script with python shell/IDLE.

In all cases, after parsing the image links,the scripts will download the chapter pages in the chapter. Enjoy!

## Requirements

You need to have python 2.7 installed to run this script. Also, [Requests](http://docs.python-requests.org/en/latest/) module is needed for the script to run, install it with `pip install requests` or `easy_install requests`. See their official link for more info.

You can also install the required packages with requirement.txt file, just use `pip install -r requirements.txt`

### Supported websites

The websites currently supported by Manga.py are listed below.

* <http://mangafox.me/>
* <http://www.mangainn.com/>
* <http://www.mangapanda.com>
* <http://mangareader.net/>
* <http://mangastream.com/> or <http://readms.com>

### Disclaimer

Use at your own liability. I suggest that you buy the manga when the volumes are out to support the writers and publishers.
