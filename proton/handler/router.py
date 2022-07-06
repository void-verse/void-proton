from proton.utils import parse_route


class Router:
    def __init__(self):
        self.routes = []

    def get(self, route: str, controller):
        parsed_route = parse_route(route)
        parsed_route["method"] = "GET"
        parsed_route["controller"] = controller
        self.routes.append(parsed_route)

    def post(self, route: str, controller):
        parsed_route = parse_route(route)
        parsed_route["method"] = "POST"
        parsed_route["controller"] = controller
        self.routes.append(parsed_route)

    def search_route(self, req):
        for route in self.routes:
            if req.method == route["method"]:
                if req.url == route["url"]:
                    return route["controller"], req
                else:
                    isSame = False
                    req_modes = req.url.split("/")
                    self_mods = route["url"].split("/")
                    if len(req_modes) == len(self_mods):
                        isSame = True
                        for i in range(len(self_mods)):
                            if str(self_mods[i]).startswith(":"):
                                pass
                            else:
                                if self_mods[i] == req_modes[i]:
                                    pass
                                else:
                                    isSame = False
                    if isSame:
                        for i in range(len(self_mods)):
                            if str(self_mods[i]).startswith(":"):
                                param = self_mods[i].replace(":", "")
                                req.params[param] = req_modes[i]
                        return route["controller"], req
            else:
                pass
        return None, req
