# -*- coding:utf-8 -*-
from clothes100.apps.base.handler import TokenHandler,MultiStandardHandler,SingleStandardHanler
from clothes100.libs.oauthlib import get_provider

class VenderListHandler(TokenHandler,MultiStandardHandler):
    _model = "vender.VenderModel"
    enable_methods = ["post","get"]

class VenderHandler(TokenHandler,SingleStandardHanler):
    _model = "vender.VenderModel"
    enable_methods = ["put","delete","get"]

handlers = [
    (r"",VenderListHandler,get_provider("vender")),
    (r"/(.*)",VenderHandler,get_provider("vender"))
]