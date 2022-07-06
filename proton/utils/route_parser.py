def parse_route(route):
    # print(route)
    parsed_route = {"url": route, "params": {}, "queries": {}}
    params = str(route).split("/")
    for param in params:
        if param.startswith(":"):
            parsed_route["params"][param.replace(':', '')] = None
    if "?" in route and "=" in route:
        queries = str(route).split("?")[1].split("&")
        for query in queries:
            parsed_route["queries"][query.split("=")[0]] = query.split("=")[1]
        parsed_route["url"] = str(route).split("?")[0]
    if parsed_route["url"].endswith("?"): parsed_route["url"] = parsed_route["url"][:-1]
    if parsed_route["url"].endswith("/"): parsed_route["url"] = parsed_route["url"][:-1]
    return parsed_route


if __name__ == "__main__":
    parse_route("/user/:id/:param?id=1234&yay=90okl")
