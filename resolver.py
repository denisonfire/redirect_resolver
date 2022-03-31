import requests


def resolver():
    # зацикленные редиректы обрабатываем с помощью перехвата исключения
    # (по дефолту requests сделает 30 редиректов до ошибки)
    try:
        r = requests.get('http://127.0.0.1:5000/cycle/one')
    except requests.TooManyRedirects:
        print('зацикленный редирект: Too many redirects')

    # множественный редирект, если мы не достигли лимита в 30 редиректов, то в результате requests вернет нужный на URL
    r = requests.get('http://127.0.0.1:5000/chain/1')
    print(f'множественный редирект: {r.url}')

    # редирект с бесконечным телом ответа обрабатываем с помощью запроса методом HEAD и ищем заголовок к ключем Location
    r = requests.head('http://127.0.0.1:5000/inf')
    print('редирект с бесконечным телом ответа: {}'.format(r.headers.get('Location')))


if __name__ == '__main__':
    resolver()
