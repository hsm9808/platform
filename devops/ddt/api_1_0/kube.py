# coding:utf-8
from flask import jsonify , render_template
from . import api
from ddt.models import Kube
from ddt.utils.response_code import RET
from ddt import db
from urllib.request import Request,urlopen

infos={
"payroll-center":10100,
"payroll-report":10101,
"accumulative":10300,
"hr-core":10105,
"time-account":10215,
"time-rule":10109,
"time-item":10209,
"time-calculate":10210,
"time-card":10212,
"time-device":10216,
"time-collector":10214,
"time-support":10217,
"time-task":10219,
"time-authinfo":80,
"time-dispatcher":80,
"schedule-config":10211,
"schedule-rule":10106,
"schedule-task":10112,
"schedule-chooser":10213,
"schedule-shift":10107,
"schedule-pos":10213,
"schedule-group":10108,
"schedule-forecast":10218,
"schedule-didi":10230,
"shared-storage":10102,
"shared-resource":10119,
"shared-control":10115,
"shared-async-excel":10110,
"shared-foundation":10104,
"shared-i18n":10114,
"shared-search":10189,
"shared-user":10103,
"shared-app-api":10120,
"shared-message":10121,
"shared-report-api":10220,
"shared-config":80,
"shared-data":10188,
"workflow-definition":10118,
"form-definition":10187,
"workflow-def":80,
"workflow-ru":80,
"custom-cayenne":18081,
"custom-sync-data":10231,
"custom-toshiba-jobs":80,
"framework-gateway":5000
}
url1 = "http://prometheus.worktrans.cn/api/v1/query?query=kube_pod_info"
url2 = []
s = []

@api.route("/get_msg",methods=["GET"])
def get_kubemsg():
    request = Request(url=url1)
    html = urlopen(request)
    data = html.read()
    strs = str(data)
    cutstrs = strs[61:-3]
    lists = eval(cutstrs)
    for a in lists:
        b = a["metric"]
        if b["namespace"] == "yu1" or b["namespace"] == "prod":
            if "consul" not in b["pod"] and "xxl" not in b["pod"] and "nginx" not in b["pod"]:
                c = '-'.join([b["pod"].split('-')[0], b["pod"].split('-')[1]])
                for i in infos:
                    if c == i:
                        url2.append("http://%s:%s/info" % (b["pod_ip"], infos[i]))
                        s.append(b["pod"])
    for i in url2:
        try:
            request = Request(url=i)
            html = urlopen(request)
            data = html.read()
            strs = str(data)
            cutstrs = strs[2:-1]
            msg_lists = eval(cutstrs)

            message = Kube(
                environment=msg_lists["serviceTag"],
                service_name=msg_lists["serviceName"],
                service_start_time=msg_lists["startTimeText"],
                git_addr=msg_lists["gitCommitId"]
            )
            db.session.add(message)
            db.session.commit()
        except:
            ex = int(i.split(':')[2].split('/')[0])
            if ex != 80:
                message = Kube(
                    environment="未获取",
                    service_name=[k for (k, v) in infos.items() if v == ex ],
                    service_start_time="未获取",
                    git_addr="未获取"
                )
                db.session.add(message)
                db.session.commit()
    return jsonify(RET.OK,errmsg="OK")

@api.route("/show_msg",methods=["GET"])
def show_kubemsg():
    message_list = Kube.query.all()
    return render_template('chart.html', message_list=message_list)