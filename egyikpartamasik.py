#!/usr/bin/env python3

import urllib.request
import json

apiVersion = '2.12'
token = ''
sites = ['facebook', 'Google', 'Microsoft', 'mozilla']
likes = []

for site in sites:
    response = urllib.request.urlopen('https://graph.facebook.com/v%s/%s?access_token=%s&fields=fan_count' % (apiVersion, site, token)).read()
    likes.append(str(json.loads(response)['fan_count']))

print(','.join(likes))
