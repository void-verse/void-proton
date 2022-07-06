from ..utils import log
from .status import get_status_text
import json

class Response:

    def __init__(self, status=200, data={}):
        self.status_code = int(status)
        self.status_text = str(get_status_text[self.status_code])
        self.status_msg = str(self.status_code) + " " + self.status_text
        self.data = json.dumps(data)
        self.headers = [
            ('Content-Type', 'application/json'),
            ('Content-Length', str(len(self.data)))
        ]

    def __str__(self):
        return log("RES", self.status_code, self.status_text)

if __name__ == '__main__':
    test = Response(status=200)
    print(test)
