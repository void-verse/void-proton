from proton.utils import msg, warn, err
from proton.handler import Router, Request, Response
from proton.db import DB


class Proton:
    def __init__(self, port=8000, debug=True):
        self.port = port
        self.host = "127.0.0.1"
        self.debug = debug
        self.router = Router()
        self.database = DB()

    def __call__(self, environ, start_response):
        response = self.request_handler(environ)
        start_response(response.status_msg, response.headers)
        return [bytes(response.data, "utf-8")]

    def request_handler(self, request_environ):
        request = Request(request_environ)
        response = Response()
        print(request)
        res_controller, request = self.router.search_route(request)
        if res_controller:
            response = res_controller(request)
        else:
            response = Response(status=404)
            print(err("REQUEST", f"URL '{request.url}' not found in server router"))
        if not isinstance(response, Response):
            response = Response(status=500)
            print(err("RESPONSE", "The controller must return a Response object"))
            print(response)
            raise TypeError(warn("The controller must return a HTTP Response object"))
        print(response)
        return response

    def set_router(self, base_path=None, router=None):
        for i in range(len(router.routes)):
            router.routes[i]["url"] = base_path + router.routes[i]["url"]
        self.router.routes.extend(router.routes)

    def set_models(self, *args):
        self.database.set_models(*args)

    def gunicorn_config(self):
        cmd = f"-b {self.host}:{self.port} --log-level warning"
        cmd += " --reload" if self.debug else ""
        return cmd
