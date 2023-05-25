#! /usr/bin/env python3
import falcon
import sqlite3
from Authenticate import Authenticate
from wsgiref.simple_server import make_server


if __name__ == '__main__':
    api = falcon.API()
    conn = sqlite3.connect('Datenbank.db')
    api.add_route('/authenticate', Authenticate(conn))
    with make_server('', 8091, api) as httpd:
        httpd.serve_forever()
