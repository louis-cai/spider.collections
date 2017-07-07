# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import requests


def post(url, payload):
    r = requests.post(url, data=payload)
    print(r.text)


def get(url):
    r = requests.get(url)
    print(r.text)


def delete(url):
    r = requests.delete(url)
    print(r.text)


def put(url, payload):
    r = requests.put(url, data=payload)
    print(r.text)


# =============================================================


def test_add():
    url = 'http://127.0.0.1:5000/club_member/add'
    payload = {'club_id': 1, 'user_id': 2}
    post(url, payload)
    pass


def test_remove():
    url = 'http://127.0.0.1:5000/club_member/remove/1/8'
    # payload = {'club_id': 8, 'user_id': 1}
    delete(url)


if __name__ == '__main__':
    # test_add()
    # test_remove()
    pass
