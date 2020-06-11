#coding:utf8
from . import api
from flask import request, jsonify, session,render_template,redirect,url_for
from ddt.models import Base,VmBase,InternetIn,IntranetIn,InternetOut,IntranetOut
from ddt import db

@api.route("/index",methods=["GET"])
def index():
   base_messages = Base.query.all()
   vmbase_messages = VmBase.query.all()
   return render_template('index.html',base_messages=base_messages,vmbase_messages=vmbase_messages)

@api.route("/show_table",methods=["GET"])
def monitor():
   inter_in = InternetIn.query.all() #公网流入带宽
   intra_in = IntranetIn.query.all() #内网流入带宽
   inter_out = InternetOut.query.all() #公网流出带宽
   intra_out = IntranetOut.query.all() #内网流出带宽
   return render_template('table.html', inter_in=inter_in,intra_in=intra_in,inter_out=inter_out,intra_out=intra_out)