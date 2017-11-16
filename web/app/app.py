from flask import Flask, redirect, make_response, Response, render_template, request, send_from_directory, url_for, jsonify
from elasticsearch import Elasticsearch
from datetime import datetime
from newsdb import get_news
import simplejson
import json
import os
import datetime

import sys
if sys.version_info.major < 3:
    reload(sys)

es_host = os.environ['DOCKER_MACHINE_IP']
print('Elastic host is {}'.format(es_host))
now = datetime.datetime.now()

# by default we don't sniff, ever
es = Elasticsearch([es_host])

app = Flask(__name__)


@app.route('/info')
def api_info():
    return jsonify(es.info())

@app.route('/nowdate')
def nowdate():
    return now.strftime("%Y-%m-%d")

@app.route('/news', methods=['GET', 'POST'])
def news():
    insdate = now.strftime("%Y-%m-%d") #"2017-11-05"
    limit = 10
    domain = ''

    if request.args.get('date'):
	insdate = request.args.get('date')
    if request.args.get('limit'):
        limit = request.args.get('limit')
    if request.args.get('domain'):
        domain = request.args.get('domain')

    info = get_news(insdate, limit, domain)

    data = {}
    data['principles'] = info
    cdata = json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4)
    return Response(cdata,  mimetype='application/json; charset=utf-8')

@app.route('/')
def api_root():
    insdate = now.strftime("%Y-%m-%d %H:%M") # "2017-11-05"
    limit = 10
    domain = ''

    if request.args.get('date'):
        insdate = request.args.get('date')
    if request.args.get('limit'):
        limit = request.args.get('limit')
    if request.args.get('domain'):
        domain = request.args.get('domain')

    dataonnews = get_news(insdate, limit, domain)
    context = {'project': "flask-bootstrap", 'author': "Anubhav Sinha", 'items':["python", "flask", "jinja2", "bootstrap", "font-awesome", "jquery"] }
    newsitems = { 'news': dataonnews }
    news = dataonnews

    return render_template('homepage.html', news = news)

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')


@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid


@app.route('/index/<id>')
def index_doc():
    doc = {
        'author': 'kimchy',
        'text': 'Elasticsearch: cool. bonsai cool.',
        'timestamp': datetime.now(),
    }
    res = es.index(index="test-index", doc_type='tweet', id=id, body=doc)
    print(res['created'])
    es.indices.refresh(index="test-index")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
