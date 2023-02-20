import requests
import json
from urllib.parse import urlparse

TOKEN = '8ac8ab4690b382ed629df286f6c744af4a922f0e'
#TOKEN = '17c09e22ad155405159ca1977542fecf00231da7'

def get_profile():
    url = 'https://api-ssl.bitly.com/v4/user'
    user  = 'Bearer '
    token = '8ac8ab4690b382ed629df286f6c744af4a922f0e'
    headers = {'Authorization': user + token}
    print(headers)

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    print(response.text)
    print(response.json())


def create_bitlink():
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    #url = 'https://api-ssl.bitly.com/v4/shorten'
    long_url = 'https://www.reddit.com/'

    # payload = {
    #     "long_url": "https://dev.bitly.com",
    #     "domain": "bit.ly",
    #     "group_guid": "Ba1bc23dE4F",
    #     "title": "Bitly API Documentation",
    #
    # }
    #
    # json_string = json.dumps(payload)
    # print(json_string)
    #return

    user  = 'Bearer '
    token = '8ac8ab4690b382ed629df286f6c744af4a922f0e'
    token = '17c09e22ad155405159ca1977542fecf00231da7'

    # headers = {
    #     'Authorization': user + token, #'Bearer 8ac8ab4690b382ed629df286f6c744af4a922f0e'
    #     'Content-Type': 'application/json',
    # }

    headers = {
        'Authorization': f'{token}',
        'Content-Type': 'application/json',
    }

    data = '{ "long_url": "https://dev.bitly.com", "domain": "bit.ly"}'
    data = {
        #"long_url": "https://dev.bitly.com",
        "long_url": long_url,
        "domain": "bit.ly"
    }
    json_string = json.dumps(data)

    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=json_string)

    #response = requests.post(url, headers=headers, data=json_string)
    response.raise_for_status()
    print('status: ', response.status_code)
    resp_json = response.json()
    print(resp_json)
    print(resp_json['link'])


def count_clicks(token, bitlink):

    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print('status: ', response.status_code)

    resp_json = response.json()
    print(resp_json)
    print(resp_json['total_clicks'])


    #return clicks_count

    # params = (
    #     ('unit', 'month'),
    #     ('units', '5'),
    #     ('unit_reference', '2006-01-02T15:04:05-0700'),
    # )
    #
    # response = requests.get('https://api-ssl.bitly.com/v4/bitlinks/bit.ly/12a4b6c/clicks', headers=headers,
    #                         params=params)
    #
    # # NB. Original query string below. It seems impossible to parse and
    # # reproduce query strings 100% accurately so the one below is given
    # # in case the reproduced version is not "correct".
    # # response = requests.get('https://api-ssl.bitly.com/v4/bitlinks/bit.ly/12a4b6c/clicks?unit=month&units=5&unit_reference=2006-01-02T15%3A04%3A05-0700', headers=headers)


def is_bitlink(link):
    parsed = urlparse(link)
    bitlink = parsed.netloc + parsed.path

    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'

    headers = {
        'Authorization': f'Bearer {TOKEN}',
        #'Authorization': f'{TOKEN}',
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print('status: ', response.status_code)

    resp_json = response.json()
    print(resp_json)

#get_profile()
#create_bitlink()

#"https://bit.ly/3lFZFpO"     for https://www.reddit.com/
#"https://es.pn/2Qw1wd7"
#bit.ly/3lFZFpO
#count_clicks(TOKEN, "bit.ly/3lFZFpO")
count_clicks(TOKEN, "es.pn/2Qw1wd7")

#is_bitlink("https://bit.ly/3lFZFpO")
#is_bitlink('http://bit.ly/2Diay99') #"long_url": "http://dvmn.org/",
#is_bitlink("https://es.pn/2Qw1wd7")
