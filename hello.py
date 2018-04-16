def app(environ, start_response):
        data = "\n".join(environ.get('QUERY_STRING').split("&"))
        start_response("200 OK", [("Content-Type", "text/plain")])
        return data
#iter([data])
