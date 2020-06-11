#coding:utf8
from . import api
from flask import request, jsonify, session,render_template,redirect,url_for
from ddt.utils.response_code import RET
from ddt.models import Device
from ddt import db

@api.route("/add_device",methods=["GET"])
def add_device():
    device_msg = eval(request.args.get("dev_name"))

    device_message=Device(
        motor_room=device_msg[0],
        rack=device_msg[1],
        device_name=device_msg[2],
        operation=device_msg[3],
        buy_time=device_msg[4],
        over_time=device_msg[5],
        detail=device_msg[6]
    )
    db.session.add(device_message)
    db.session.commit()
    # return jsonify(errno=RET.OK, errmsg="OK")
    return jsonify(errno=RET.OK, errmsg="OK")

@api.route("/show_device",methods=["GET"])
def show_device():
    device_messages = Device.query.all()
    return render_template('device.html',device_messages=device_messages)

@api.route("/change_device",methods=["GET"])
def change_device():
    device_msg = eval(request.args.get("change_message"))
    result = Device.query.filter(Device.device_id == device_msg[0]).first()
    if device_msg[1] != "":
        result.motor_room = device_msg[1]
    if device_msg[2] != "":
        result.rack = device_msg[2]
    if device_msg[3] != "":
        result.device_name = device_msg[3]
    if device_msg[4] != "":
        result.operation = device_msg[4]
    if device_msg[5] != "":
        result.buy_time = device_msg[5]
    if device_msg[6] != "":
        result.over_time = device_msg[6]
    if device_msg[7] != "":
        result.detail = device_msg[7]
    db.session.commit()
    # print(result.motor_room)
    return jsonify(errno=RET.OK, errmsg="OK")

@api.route("/delete_device",methods=["GET"])
def delete_device():
    device_id = request.args.get("device_id")

    delete_result = Device.query.get(device_id)
    db.session.delete(delete_result)
    db.session.commit()
    return redirect(url_for("api_1_0.show_device"))
