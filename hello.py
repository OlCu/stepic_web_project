def app(environ, start_response):                                                                 
    resp = environ['QUERY_STRING'].split('&')                                   
    resp = [item.encode('utf-8')+b'\r\n' for item in resp]                      
    start_response("200 OK", [("Content-Type", "text/plain")])                  
    return resp                                                                 
                                             
