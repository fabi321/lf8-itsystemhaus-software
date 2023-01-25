import sqlite3
from typing import Optional
import falcon
import json


class Authenticate:
    def __init__(self, db_connection: sqlite3.Connection):
        self.db_connection: sqlite3.Connection = db_connection

    def on_get(self, request: falcon.Request, response: falcon.Response):
        parameters: dict[str, str] = falcon.uri.parse_query_string(request.query_string)
        if 'user_id' not in parameters or 'password' not in parameters:
            response.status = falcon.HTTP_400
            response.body = '{}'
            return
        cur: sqlite3.Cursor = self.db_connection.cursor()
        result = cur.execute(
            'select Benutzer_ID, Vorname, Name from Benutzer where Benutzer_ID = ? and Passwort = ?',
            (parameters['user_id'], parameters['password'])
        )
        row: Optional[sqlite3.Row] = result.fetchone()
        if row:
            user_id: str = row[0]
            vorname: Optional[str] = row[1]
            nachname: Optional[str] = row[2]
            result = cur.execute(
                'select Gruppen_ID, g.Name from Benutzergruppe inner join Gruppe g using (Gruppen_ID) where Benutzer_ID = ?',
                (user_id,)
            )
            rows: list[tuple[int, str]] = result.fetchall()
            gruppen: list[tuple[int, str]] = [tuple(row) for row in rows]
            response.body = json.dumps({'user_id': user_id, 'vorname': vorname, 'nachname': nachname, 'gruppen': gruppen})
        else:
            response.status = falcon.HTTP_401
            response.body = '{}'
