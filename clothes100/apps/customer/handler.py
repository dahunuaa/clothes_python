#-*- coding:utf-8 -*-

from clothes100.apps.base.handler import TokenHandler,MultiStandardHandler,SingleStandardHanler
from clothes100.libs.oauthlib import get_provider

class CustomerListHandler(TokenHandler,MultiStandardHandler):
    _model = "customer.CustomerModel"
    enable_methods = ["post","get"]

class CustomerHandler(TokenHandler,SingleStandardHanler):
    _model = "customer.CustomerModel"
    enable_methods = ['get','put','delete']

handlers =[
    (r"",CustomerListHandler,get_provider("customer")),
    (r"/(.*)",CustomerHandler,get_provider("customer"))
]