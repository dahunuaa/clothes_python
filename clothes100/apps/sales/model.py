# -*- coding:utf-8 -*-

import clothes100.apps.base.model as model
from clothes100.libs.datatypelib import *

class SalesModel(model.StandCURDModel):
    _coll_name = "sales"
    _columns = [
        ("customer_mobile",MobileDT(required=True)),
        ("customer_name", StrDT(required=True)),
        # ("sale_time",DatetimeDT(required=True)),
        ("clerk",StrDT(required=True)),
        ("store", StrDT(required=True)),
        ("goods",ListDT(required=True)),
        ("pay_type",ConstDT(const="PAY_TYPE",default="cash")),
        ("pay_amounts",StrDT(required=True)),
        ("debt",StrDT(default=0)),
        ("sum_debt",StrDT()),
        ("sum_amount",StrDT()),
        ("remark",StrDT())
    ]

    # def before_create(self,object):
    #     # 修改客户的欠款金额
    #     pass
