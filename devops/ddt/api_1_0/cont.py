# coding:utf-8
from flask import jsonify , render_template,request
from . import api
from ddt.models import Container
from ddt.utils.response_code import RET
from ddt import db
from urllib.request import Request,urlopen
from kubernetes import client,config
import requests,yaml
requests.packages.urllib3.disable_warnings()

token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi11c2VyLXRva2VuLWdjYnFnIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluLXVzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiJlNDIxYmNiZC1lMWE4LTQxM2YtYWM5ZS0xMGEzZjFmZjRiMDIiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06YWRtaW4tdXNlciJ9.fx07gZ5nOkMlfRmq0yCB4w1s5djrym7CW3b3-l3CaMyb2AQ8iE7sT_6FQs7nNim-fjnSkgaJB1tocSzxVVCBT6WylgN7XXpkfzkgjJO18dVgnHH0unZbAj3AN_k0pLcf1BfHS82zAaYlF_gn0i0b9cL3nxpvQ1r_dLDlDPXR4juAqubz0brYYyg4LZZ2-3XblSYjWKHvsSoXtw11lhl3B0WjluVlWO9tuqTOOlefq1ow1p31Y1RkPqLKht0VSczTTDX_0Pr6qmntGq2LgvF8toruXTMFurdGnhfxbiQypDa4JQewSeRFHzAwQ-JSj_kor9qXh-zB87O6nWNRpO_hHg"
configuration = client.Configuration()

host = 'https://123.56.80.143:6443'
configuration.host = host
configuration.verify_ssl = False
configuration.api_key = {"authorization": "Bearer "+ token}
client.Configuration.set_default(configuration)
v1 = client.CoreV1Api()


@api.route("/show_container",methods=["GET"])
def show_container():
    pod_messages = Container.query.all()
    return render_template('pod.html',pod_messages=pod_messages)

@api.route("/image_update",methods=["GET"])
def image_update():
    image_msg = eval(request.args.get("msg"))
    old_resp = v1.read_namespaced_pod(namespace=image_msg[0], name=image_msg[1])
    old_resp.spec.containers[0].image = "%s:%s"%(image_msg[2],image_msg[3])
    # 修改镜像
    v1.patch_namespaced_pod(namespace=image_msg[0], name=image_msg[1], body=old_resp)
    return jsonify(errno=RET.OK, errmsg="OK")

@api.route("/create_pod",methods=["GET"])
def create_pod():
    pod_msg = eval(request.args.get("pod_message"))
    with open(r"C:\Users\Administrator\Desktop\test\demo.yaml", encoding='utf-8') as f:
        dep = yaml.safe_load(f)
        dep["apiVersion"] = pod_msg[0]
        dep["metadata"]["name"] = pod_msg[1]
        dep["spec"]["containers"][0]["name"] = pod_msg[2]
        dep["spec"]["containers"][0]["image"] = pod_msg[3]
        v1.create_namespaced_pod(body=dep, namespace="default")
    return jsonify(errno=RET.OK, errmsg="OK")