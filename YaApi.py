import requests


def put_file(derictories, token):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    params = {"path": f'{derictories}'}
    response = requests.put(url, headers=headers, params=params)
    if response.status_code != 201:
        return response.json()['error']
    return f'Папка {derictories} создана в директории'



if __name__ == '__main__':
    token = ''
    derictories = "New papka"
    print(put_file(derictories, token))
