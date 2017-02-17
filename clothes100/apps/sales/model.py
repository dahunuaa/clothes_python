# -*- coding:utf-8 -*-

import clothes100.apps.base.model as model
from clothes100.libs.datatypelib import *

class SalesModel(model.StandCURDModel):
    _coll_name = "sales"
    _columns = [
        ("customer_mobile",MobileDT()),
        ("customer_name", StrDT()),
        # ("sale_time",DatetimeDT(required=True)),
        ("clerk",StrDT(required=True)),
        ("store", StrDT(required=True)),
        ("goods",ListDT(required=True)),
        ("pay_type",ConstDT(const="PAY_TYPE",default="cash")),
        ("pay_amounts",StrDT(required=True)),
        ("debt",IntDT(default=0)),
        ("sum_debt",IntDT()),
        ("sum_amount",IntDT()),
        ("remark",StrDT())
    ]

    # 修改客户的欠款金额
    #分三种类型 1、有客户资料的 2、没有客户资料的但是提供手机号的 3、不提供手机号的就直接不添加客户，直接开单了
    def before_create(self, object):
        _customer_mobile = self.get_argument("customer_mobile")
        _sum_debt = self.get_argument("sum_debt")
        if _customer_mobile is not None and _customer_mobile !="":
            customer_model = model.BaseModel.get_model("customer.CustomerModel")
            customer_coll =customer_model.get_coll()
            customer = customer_coll.find_one({"customer_mobile":_customer_mobile})
            if customer is not None:
                customer["sum_debt"] = _sum_debt
                customer_coll.save(customer)
            else:
                # 如果顾客表中没有该用户，则在该用户消费的时候，自动在顾客表中创建该用户
                new_customer = {}
                new_customer["customer_mobile"] = _customer_mobile
                new_customer["sum_debt"]=_sum_debt
                customer_coll.save(new_customer)
        else:
            pass
        return  object


