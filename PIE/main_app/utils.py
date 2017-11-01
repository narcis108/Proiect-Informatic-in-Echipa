import json
import urllib.request
import urllib.parse

tmdb_url = 'https://api.themoviedb.org/3/find/'
api_key = '3986fda552c95cef5c70504165885970'
language = 'en-US'
external_source = 'imdb_id'


def query_tmdb(imdb_link):
    """ get movie info (json) from IMDB """
    imdb_id = convert_imdb_link(imdb_link)
    params = urllib.parse.urlencode({'api_key': api_key, 'language': language, 'external_source': external_source})
    url = "%s%s?%s" % (tmdb_url, imdb_id, params)
    f = urllib.request.urlopen(url)
    return json.loads(f.read())


def convert_imdb_link(link):
    imdb_id = link[5:].split('/')
    for element in imdb_id:
        if 'tt' in element:
            print(element)
            return element
