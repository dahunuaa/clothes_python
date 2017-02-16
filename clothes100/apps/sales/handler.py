# -*- coding:utf-8 -*-
from clothes100.apps.base.handler import TokenHandler,MultiStandardHandler,SingleStandardHanler
from clothes100.libs.oauthlib import get_provider
from  clothes100.libs.loglib import get_logger


class SalesListHandler(TokenHandler,MultiStandardHandler):
    _model = "sales.SalesModel"
    enable_methods = ["post","get"]

class SalesHandler(TokenHandler,SingleStandardHanler):
    _model = "sales.SalesModel"
    enable_methods = ["put","get","delete"]

handlers= [
    (r"",SalesListHandler,get_provider("sales")),
    (r"/(.*)",SalesHandler,get_provider("sales"))
]