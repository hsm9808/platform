#coding:utf8

from flask import Blueprint

#创建蓝图对象
api = Blueprint("api_1_0",__name__)

from . import login,jk,kube,device,zabbix,cont
