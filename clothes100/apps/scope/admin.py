# -*- coding:utf-8 -*-
from clothes100.apps.base.handler import TokenHandler,MultiStandardHandler,SingleStandardHanler
from clothes100.libs.oauthlib import get_provider

class AdminScopeListHandler(MultiStandardHandler,TokenHandler):
    _model = "scope.ScopeModel"

class AdminScopeHandler(SingleStandardHanler,TokenHandler):
    _model = "scope.ScopeModel"

handlers =[
    (r"",AdminScopeListHandler,get_provider('scope')),
    (r"/(.*)",AdminScopeHandler,get_provider('scope'))
]