import requests
from urllib.parse import urlparse
import os
import argparse


BITLY_API_SHORTEN_URL = 'https://api-ssl.bitly.com/v4/shorten'


def shorten_link(token, long_url):
    headers = {
        'Authorization': f'{token}',
    }

    payload = {
        "long_url": long_url,
    }

    response = requests.post(BITLY_API_SHORTEN_URL, headers=headers, json=payload)
    response.raise_for_status()

    return response.json()['link']


def count_clicks(token, link):
    parsed_link = urlparse(link)
    bitlink = f'{parsed_link.netloc}{parsed_link.path}'

    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    return response.json()['total_clicks']


def is_bitlink(token, link):
    parsed_link = urlparse(link)
    bitlink = f'{parsed_link.netloc}{parsed_link.path}'

    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(url, headers=headers)
    return response.ok


def main():
    token = os.environ['BITLY_TOKEN']
    
    parser = argparse.ArgumentParser()
    parser.add_argument('link', help='ссылка bitly или любая ссылка https')
    args = parser.parse_args()
    user_link = args.link

    try:
        if is_bitlink(token, user_link):
            print(count_clicks(token, user_link))
        else:
            print(shorten_link(token, user_link))
    except requests.exceptions.HTTPError as ex:
        print(ex)


if __name__ == '__main__':
    main()
