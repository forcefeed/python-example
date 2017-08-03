#!/usr/bin/env python

from __future__ import print_function

import json
import requests
from pprint import pprint
from sseclient import SSEClient

url = 'http://forcefeed.ir/sse'

print('Connecting to forcefeed...')
client = SSEClient(requests.get(url, stream=True))

nevents = 0
try:
    print('Receiving events...')
    for event in client.events():
        pprint(json.loads(event.data))
        nevents += 1
except KeyboardInterrupt:
    print()

print('Received {} events.'.format(nevents))
