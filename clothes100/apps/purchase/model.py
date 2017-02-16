# -*- coding:utf-8 -*-
import clothes100.apps.base.model as model
from clothes100.libs.datatypelib import *

class PurchaseModel(model.StandCURDModel):
    _coll_name = "purchase"
    _columns = [
        ("storage_date",DatetimeDT(required=True)),
        ("order_num",StrDT(required=True)),
        ("goods_num",StrDT(required=True)),
        ("goods_name",StrDT()),
        ("color",ConstDT(const="COLOR",default="average")),
        ("dress_type",ConstDT(const='DRESS_TYPE',default='women')),#添加一个选择男女衣服型号的字段，尺码男女不一样
        ("size",StrDT(default="average")),
        ("component",ConstDT(const='MATERIAL',default='cotton')),
        ("amounts",StrDT()),
        ("unit_price",StrDT()),
        ("sum",StrDT()),
        ("retail_price",StrDT()),
        ("pack_price",StrDT()),
        ("friends_price",StrDT()),
        ("sale_price1",StrDT()),
        ("sale_price2",StrDT()),
        ("vender",StrDT()),
        ("pay_type",ConstDT(const="PAY_TYPE",default="cash")),
        ("payment",StrDT()),
        ("debt",StrDT()),
        ("bar_code",StrDT()),#前端通过扫描条形码获得的数字
        ("image_list",ListDT())
    ]