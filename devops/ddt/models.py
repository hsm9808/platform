# -*- coding:utf-8 -*-

from datetime import datetime
from . import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    """用户"""
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # 用户编号
    username = db.Column(db.String(32), unique=True, nullable=False)  # 用户名字
    password = db.Column(db.String(128), nullable=False)  # 加密的密码

class Jenkins_Info(db.Model):
    """jenkins信息"""
    __tablename__ = "build_info"
    jenkins_id = db.Column(db.Integer, primary_key=True)
    jenkins_name = db.Column(db.String(32), unique=False, nullable=False)
    consul_url = db.Column(db.String(1024), unique=True, nullable=False)
    start_time = db.Column(db.String(32), unique=False, nullable=False)
    result = db.Column(db.String(32), unique=False, nullable=False)
    username = db.Column(db.String(32), unique=False, nullable=False)

class Kube(db.Model):
    __tablename__ = "kube_info"
    kube_id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String(32), unique=False, nullable=False)
    service_name = db.Column(db.String(1024), unique=False, nullable=False)
    service_start_time = db.Column(db.String(32), unique=False, nullable=False)
    git_addr = db.Column(db.String(32), unique=False, nullable=False)

class Device(db.Model):
    __tablename__ = "device_info"
    device_id = db.Column(db.Integer, primary_key=True)
    motor_room = db.Column(db.String(32), unique=False, nullable=False)
    rack = db.Column(db.String(32), unique=False, nullable=False)
    device_name = db.Column(db.String(32), unique=False, nullable=False)
    operation = db.Column(db.String(32), unique=False, nullable=False)
    buy_time = db.Column(db.String(32), unique=False, nullable=False)
    over_time = db.Column(db.String(32), unique=False, nullable=False)
    detail = db.Column(db.String(1024),unique=False,nullable=False)

class Base(db.Model):
    __tablename__ = "system"
    CPU_LOAD = db.Column(db.String(32),primary_key=True)
    DISK = db.Column(db.String(32))
    USED = db.Column(db.String(32))
    FREE = db.Column(db.String(32))

class VmBase(db.Model):
    __tablename__ = "vmsystem"
    CPU_LOAD = db.Column(db.String(32),primary_key=True)
    DISK = db.Column(db.String(32))
    USED = db.Column(db.String(32))
    FREE = db.Column(db.String(32))

class InternetIn(db.Model):
    __tablename__ = "ain"
    monitor_time = db.Column(db.String(32), primary_key=True)
    InternetInRate = db.Column(db.String(32)) #公网流入带宽

class IntranetIn(db.Model):
    __tablename__ = "bin"
    monitor_time = db.Column(db.String(32), primary_key=True)
    IntranetInRate = db.Column(db.String(32)) #内网流入带宽

class InternetOut(db.Model):
    __tablename__ = "aout"
    monitor_time = db.Column(db.String(32), primary_key=True)
    InternetOutRate = db.Column(db.String(32)) #公网流出带宽

class IntranetOut(db.Model):
    __tablename__ = "bout"
    monitor_time = db.Column(db.String(32), primary_key=True)
    IntranetOutRate = db.Column(db.String(32)) #内网流出带宽

class Container(db.Model):
    __tablename__ = "pod"
    pod_name = db.Column(db.String(108), primary_key=True)
    pod_namespace = db.Column(db.String(108))
    pod_ip = db.Column(db.String(64))
    pod_image = db.Column(db.String(108))