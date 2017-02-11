# -*- coding:utf-8 -*-

from clothes100.apps.base.handler import TokenHandler,SingleStandardHanler,MultiStandardHandler
from clothes100.libs.loglib import get_logger
from clothes100.libs.oauthlib import get_provider

logger = get_logger("debug")

class ScopeHandler(SingleStandardHanler,TokenHandler):
    _model = "scope.ScopeModel"
    peivate =False
    enable_methods = ["get"]

    def get(self):
        return super(ScopeHandler,self).get(self.scope['_id'])

handlers = [
    (r"",ScopeHandler,get_provider('scope'))
]