# -*- coding:utf-8 -*-
__author__ = 'zhaojm'


class Error302(Exception):
    def __init__(self):
        self.message = "error 302"
        pass


class Error403(Exception):
    def __init__(self):
        self.message = "error 403"
        pass


class Error404(Exception):
    def __init__(self):
        self.message = "error 404"
        pass


class ErrorStatusCode(Exception):
    def __init__(self, status_code):
        self.message = "error status code: %s" % status_code
        pass
