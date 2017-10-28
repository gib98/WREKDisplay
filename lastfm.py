##### coding: utf-8 #####

# Simple last.fm interface for retrieving album art
# (and possibly other information). Scrapped authentication
# and scrobble functionality since we don't need it!
# Noah Roberts :)

# Uncomment & copy & paste this into main file to use this interface:
#######################################################
# import sys
# import os
#
# # Change this path to true path of project directory
# sys.path.append(os.path.abspath('./'))
#
# from env import *
# from lastfm import *
#######################################################

import sys
import os
import requests
import json
import hashlib
import six

class lastfm():

    # constructor
    def __init__(self):

        self.apiKey = os.environ.get('LastApiKey')
        self.secret = os.environ.get('LastSecret')

        if self.apiKey == '<YOUR API KEY>' or self.secret == '<YOUR SECRET>':
            raise ApiKeyNotSetException()

    # returns string holding image url
    def getAlbumArt(self, artist, album):

        payload = {'method':'album.getInfo',
                   'artist':artist,
                   'album':album,
                   'api_key':self.apiKey}

        payload['api_sig'] = self.genApiSig(payload)
        payload['format'] = 'json'

        response = requests.get('http://ws.audioscrobbler.com/2.0/?', payload)

        if response.status_code == 200:
            # Success!
            response = response.json()
            image = response['album']['image'][2]['#text']
            return image
        else:
            return 'failure'

    # returns a dict with some cool stuff
    def getArtistInfo(self, artist):

        payload = {'method':'artist.getInfo',
                   'artist':artist,
                   'api_key':self.apiKey}

        payload['api_sig'] = self.genApiSig(payload)
        payload['format'] = 'json'

        response = requests.get('http://ws.audioscrobbler.com/2.0/?', payload)

        if response.status_code == 200:
            response = response.json()

            # return an ugly dict (but thats ok for now)
            info = {}
            info['status'] = 'success'
            info['name'] = response['artist']['name']
            info['listeners'] = response['artist']['stats']['listeners']
            info['playcount'] = response['artist']['stats']['playcount']
            info['bio'] = response['artist']['bio']['summary']
            
            return info

        else:
            return {'status':'failure'}


    def genApiSig(self, dataToHash):

            sigStr = ''
            for key in sorted(dataToHash):
                sigStr += key + dataToHash[key]

            sigStr += self.secret
            return md5(sigStr)


# helper functions

def md5(text):
    h = hashlib.md5(formatUnicode(text).encode("utf-8"))
    return h.hexdigest()


def formatUnicode(text):

    if isinstance(text, six.binary_type):
        return six.text_type(text, "utf-8")
    elif isinstance(text, six.text_type):
        return text
    else:
        return six.text_type(text)


# exception
class ApiKeyNotSetException(Exception):
    print('Please set your API key and secret (obtained from last.fm) in env.py')
    pass