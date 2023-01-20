#! /usr/bin/env python3
import falcon
import sqlite3
from Authenticate import Authenticate


if __name__ == '__main__':
    api = falcon.API()
    conn = sqlite3.connect('../Datenbank.db')
    authentication_endpoint = Authenticate()
    api.add_route('/authenticate', authentication_endpoint)
