# -*- coding:utf-8 -*-
import clothes100.apps.base.model as model
from clothes100.libs.datatypelib import *

class VenderModel(model.StandCURDModel):
    _coll_name = "vender"
    _columns =[
        ("vender_name",StrDT(required=True)),
        ("legal_re",StrDT()),
        ("permit_no",StrDT()),
        ("address",StrDT(required=True)),
        ("mobile",MobileDT(required=True)),
        ("remark",StrDT())
    ]