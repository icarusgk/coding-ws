import requests

uri = "http://127.0.0.1:8000"


def main():
    response = make_post()
    print(response)


def login():
    return requests.post(f'{uri}/login', data={
        'username': 'icarus',
        'password': '1234'
    })


def make_post():
    return requests.post(f'{uri}/api/post', data={
        'body': 'hi!'
    })


if __name__ == '__main__':
    main()

