import falcon
import requests


class Authenticate:
    def __init__(self):
        ...

    def on_get(self, request: falcon.Request, response: falcon.Response):
        parameters: dict[str, str] = falcon.uri.parse_query_string(request.query_string)
        if 'user_id' not in parameters or 'password' not in parameters:
            response.status = falcon.HTTP_400
            response.body = '{}'
            return
        resp: requests.Response = requests.get('http://localhost:8091', parameters)
        if resp.status_code == 200:
            response.status = falcon.HTTP_200
        else:
            response.status = falcon.HTTP_403
        response.body = resp.text

