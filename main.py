import requests
import json
from urllib.parse import urlparse
import os
import argparse

TOKEN = os.environ['TOKEN_BITLY']
#TOKEN = '8ac8ab4690b382ed629df286f6c744af4a922f0e'
URL_BITLY_API_SHORTEN = 'https://api-ssl.bitly.com/v4/shorten'


def shorten_link(token, long_url):
    headers = {
        'Authorization': f'{token}',
        'Content-Type': 'application/json',
    }

    data_for_post = {
        "long_url": long_url,
        "domain": "bit.ly"
    }

    response = requests.post(URL_BITLY_API_SHORTEN, headers=headers, data=json.dumps(data_for_post))
    response.raise_for_status()

    resp_json = response.json()
    return resp_json['link']


def count_clicks(token, link):
    parsed = urlparse(link)
    bitlink = f'{parsed.netloc}{parsed.path}'

    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    resp_json = response.json()
    return resp_json['total_clicks']


def is_bitlink(token, link):
    parsed = urlparse(link)
    bitlink = f'{parsed.netloc}{parsed.path}'

    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(url, headers=headers)
    return response.ok


def main():
    #user_link = input("Введите ссылку: ")
    parser = argparse.ArgumentParser()
    parser.add_argument('link', help='ссылка bitly или любая ссылка https')
    args = parser.parse_args()
    user_link = args.link

    try:
        if is_bitlink(TOKEN, user_link):
            print(count_clicks(TOKEN, user_link))
        else:
            print(shorten_link(TOKEN, user_link))
    except requests.exceptions.HTTPError as ex:
        print(ex)


if __name__ == '__main__':
    main()
