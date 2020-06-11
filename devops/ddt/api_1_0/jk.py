# coding:utf-8
import jenkins,datetime,time,json
from flask import Flask , render_template,request,redirect,url_for,session
from . import api
from ddt.models import Jenkins_Info
from ddt import db

url = 'http://123.56.80.143:8088'
username = 'admin'
password = 'password'  #利用api-token更好
timeout = 100
server = jenkins.Jenkins(url,username,password,timeout)
server.get_whoami()

@api.route("/jenkins-build",methods=["GET"])
def build():
    job_name = request.args.get("bd_name1")
    parameters1 = {'action': 'Deploy'}
    str_job_name = eval(job_name)
    for i in str_job_name:
        server.build_job(i, parameters=parameters1)
        time.sleep(10)
        bd_number = server.get_job_info(i)['lastBuild']['number'] #构建的次数
        build_state = server.get_build_info(i, bd_number)['timestamp'] #构建的时间
        bd_consul_url = server.get_build_info(i,bd_number)["url"] #日志信息的url
        bd_console_url = bd_consul_url.replace('8080','8088')
        build_time = datetime.datetime.utcfromtimestamp(float(build_state) / 1000 + 3600 * 8).strftime(
            '%Y-%m-%d %H:%M:%S')
        build_result = server.get_build_info(i, bd_number)["result"]
        if build_result is None:
            build_result = 'building'
        else:
            build_result = build_result
        # finish_time = datetime.datetime.utcfromtimestamp(
        #     float(build_state) / 1000 + 3600 * 8 + float(duration) / 1000).strftime('%Y-%m-%d %H:%M:%S')

        bd_message = Jenkins_Info(
            username = session["username"],
            jenkins_name = i,
            start_time= build_time,
            consul_url=bd_console_url,
            result=build_result
        )
        db.session.add(bd_message)
        db.session.commit()

    return redirect(url_for("api_1_0.jek"))

@api.route("/jenkins-rollback",methods=["GET"])
def rollback():
    job_name = request.args.get("bd_name2")
    parameters2 = {'action': 'RollBack'}
    str_job_name = eval(job_name)
    for i in str_job_name:
        server.build_job(i, parameters=parameters2)
        time.sleep(10)
        bk_number = server.get_job_info(i)['lastBuild']['number'] #构建的次数
        rollback_state = server.get_build_info(i, bk_number)['timestamp'] #构建的时间
        bk_consul_url = server.get_build_info(i,bk_number)["url"] #日志信息的url
        bk_console_url = bk_consul_url.replace('8080','8088')
        build_time = datetime.datetime.utcfromtimestamp(float(rollback_state) / 1000 + 3600 * 8).strftime(
            '%Y-%m-%d %H:%M:%S')
        rollback_result = server.get_build_info(i, bk_number)["result"]
        if rollback_result is None:
            rollback_result = 'building'
        else:
            rollback_result = rollback_result
        # finish_time = datetime.datetime.utcfromtimestamp(
        #     float(build_state) / 1000 + 3600 * 8 + float(duration) / 1000).strftime('%Y-%m-%d %H:%M:%S')

        bk_message = Jenkins_Info(
            username = session["username"],
            jenkins_name = i,
            start_time= build_time,
            consul_url=bk_console_url,
            result=rollback_result
        )
        db.session.add(bk_message)
        db.session.commit()

    return redirect(url_for("api_1_0.jek"))

@api.route("/jenkins-info/",methods=["GET"])
def jek():
    msg_list = Jenkins_Info.query.all()
    return render_template('tab-panel.html',msg_list=msg_list)

@api.route("/jenkins-check",methods=["GET"])
def check_result():
    a = Jenkins_Info.query.filter_by(result="building").all()
    for i in a:
        lastbuildNumber = server.get_job_info(i.jenkins_name)['lastBuild']['number']
        build_state = server.get_build_info(i.jenkins_name, lastbuildNumber)["result"]
        if build_state is None:
            build_state = 'building'
        else:
            build_state = build_state
        i.result = build_state
    db.session.commit()
    return redirect(url_for("api_1_0.jek"))
