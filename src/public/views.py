"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template
from .forms import LogUserForm, secti,masoform
from ..data.database import db
from ..data.models import LogUser, Stats
from datetime import datetime, timedelta
import urllib2
import json
import os

blueprint = Blueprint('public', __name__)
os.environ['no_proxy']='*'

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')

@blueprint.route('/loguserinput',methods=['GET', 'POST'])
def InsertLogUser():
    form = LogUserForm()
    if form.validate_on_submit():
        LogUser.create(**form.data)
    return render_template("public/LogUser.tmpl", form=form)

@blueprint.route('/loguserlist',methods=['GET'])
def ListuserLog():
    pole = db.session.query(LogUser).all()
    return render_template("public/listuser.tmpl",data = pole)

@blueprint.route('/secti', methods=['GET','POST'])
def scitani():
    form = secti()
    if form.validate_on_submit():
        return render_template('public/vystup.tmpl',hod1=form.hodnota1.data,hod2=form.hodnota2.data,suma=form.hodnota1.data+form.hodnota2.data)
    return render_template('public/secti.tmpl', form=form)

@blueprint.route('/maso', methods=['GET','POST'])
def masof():
    form = masoform()
    if form.validate_on_submit():
        return render_template('public/masovystup.tmpl',hod1=form.hodnota1.data,hod2=form.hodnota2.data,suma=form.hodnota1.data+form.hodnota2.data)
    return render_template('public/maso.tmpl', form=form)

def getData():
    r = urllib2.urlopen('http://192.168.10.1:5001/data.json')
    data = json.load(r)
    return data


@blueprint.route('/stats', methods=['GET','POST'])
def stats():
    now = datetime.now()
    now_minus_10 = now - timedelta(minutes=10)
    data = list(db.session.query(Stats).filter(Stats.cas>now_minus_10).all())
    return render_template('public/stats.tmpl', data=data)

