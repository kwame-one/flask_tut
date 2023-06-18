from time import time

from flask_http_middleware import BaseHTTPMiddleware


class LoggerMiddleware(BaseHTTPMiddleware):
    def __init__(self):
        super().__init__()

    def dispatch(self, request, call_next):
        t0 = time()
        response = call_next(request)
        response_time = time() - t0
        response.headers.add("response_time", response_time)
        print(response_time)
        return response
