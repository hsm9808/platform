#coding:utf8
from . import api
from flask import request, jsonify, session,current_app
from ddt.utils.response_code import RET
from ddt.models import User


@api.route("/session",methods=["POST"])
def login():
    """登录"""
    req_dict = request.get_json()
    username = req_dict.get("username")
    password = req_dict.get("password")
    #参数校验
    if not all([username,password]):
        return jsonify(errno=RET.PARAMERR,errmsg="参数不完整")
    #从数据库中根据名字查询用户对象
    try:
        user = User.query.filter_by(username=username).first()
    except :
        return jsonify(errno=RET.DBERR,errmsg="无此用户")
    #密码对比失败
    if user is None or password !=user.password:
        return jsonify(errno=RET.DATAERR,errmsg="用户名或密码错误")
    #密码对比成功
    session["username"]=user.username
    return jsonify(errno=RET.OK,errmsg="登录成功")

@api.route("/sessions",methods=["GET"])
def check_login():
    """检查登录状态"""
    username = session.get("username")
    if username is not  None:
        return jsonify(errno=RET.OK,errmsg="true",data={"username":username})
    else:
        return jsonify(errno=RET.SESSIONERR,errmsg="false")

@api.route("/sessions",methods=["DELETE"])
def logout():
    """登出"""
    csrf_token = session.get("csrf_token")
    session.clear()
    session["csrf_token"] = csrf_token
    return jsonify(errno=RET.OK,errmsg="OK")