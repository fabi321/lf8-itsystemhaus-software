#! /usr/bin/env python3
import falcon
import sqlite3
from wsgiref.simple_server import make_server

from Authenticate import Authenticate


if __name__ == '__main__':
    api = falcon.API()
    conn = sqlite3.connect('Datenbank.db')
    api.add_route('/authenticate', Authenticate())
    with make_server('', 8090, api) as httpd:
        httpd.serve_forever()
