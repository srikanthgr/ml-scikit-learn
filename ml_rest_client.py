#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 08:45:21 2021

@author: srikanth
"""

import json
import requests

url = 'http://127.0.0.1:8002/model'

request_data = json.dumps({'age':'40', 'salary':20000})
response = requests.post(url,request_data)
print (response.text)
