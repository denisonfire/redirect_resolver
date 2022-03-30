import requests


def resolver():
    # зацикленный редирект
    try:
        r = requests.get('http://127.0.0.1:5000/cycle/one')
    except requests.TooManyRedirects:
        print('зацикленный редирект: Too many redirects')

    # множественный редирект
    r = requests.get('http://127.0.0.1:5000/chain/1')
    print(f'множественный редирект: {r.url}')

    # редирект с бесконечным телом ответа
    r = requests.head('http://127.0.0.1:5000/inf')
    print('редирект с бесконечным телом ответа: {}'.format(r.headers.get('Location')))


if __name__ == '__main__':
    resolver()
