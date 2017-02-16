# -*- coding:utf-8 -*-
import clothes100.apps.base.model as model
from clothes100.libs.datatypelib import *

class CustomerModel(model.StandCURDModel):
    _coll_name = "customer"
    _columns= [
        ("customer_mobile",MobileDT(required=True)),
        ("customer_name",StrDT()),
        ("customer_birth",DatetimeDT()),
        ("sex",StrDT(default="男")),
        ("wx_num",StrDT()),
        ("customer_type",ConstDT(const="CUSTOMER_TYPE",default="common_friend")),
        ("sum_debt", IntDT(default=0)),
        ("remark",StrDT()),
    ]