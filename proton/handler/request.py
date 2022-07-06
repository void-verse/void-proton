from proton.utils import log, parse_route
import json


class Request:
    def __init__(self, environ):
        self.method = environ["REQUEST_METHOD"]
        parsed_route = parse_route(f"{environ['PATH_INFO']}?{environ['QUERY_STRING']}")
        self.url = parsed_route["url"]
        self.params = parsed_route["params"]
        self.queries = parsed_route["queries"]
        self.content_length = int(environ.get("CONTENT_LENGTH", 0))
        encoded_data = environ["wsgi.input"].read(self.content_length)
        self.data = json.loads(encoded_data.decode("utf-8"))

    def __str__(self):
        return log("REQ", self.method, self.url)
