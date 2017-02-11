# -*- coding:utf-8 -*-
from clothes100.apps.base.handler import TokenHandler,MultiStandardHandler,SingleStandardHanler
from clothes100.libs.oauthlib import  get_provider

class PurchaseListHandler(MultiStandardHandler,TokenHandler):
    _model = "purchase.PurchaseModel"
    enable_methods = ["post","get"]

class PurchaseHandler(SingleStandardHanler,TokenHandler):
    _model = "purchase.PurchaseModel"
    enable_methods = ["get","put","delete"]

handlers =[
    (r"",PurchaseListHandler,get_provider("purchase")),
    (r"/(.*)",PurchaseHandler,get_provider("purchase"))
]