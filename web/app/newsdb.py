#!/usr/bin/python
from __future__ import unicode_literals
import MySQLdb
from urlparse import urlparse
import datetime

def mysql_connection(host):
    db = MySQLdb.connect(host=host,    # your host, usually localhost
                     port=3306,
                     user="root",         # your username
                     passwd="root",  # your password
                     charset="utf8", use_unicode=True,
                     db="crawler2017")        # name of the data base

    cursor = db.cursor()
    return cursor

def get_news(insertdate, limit, domain):
    cur = mysql_connection('test-mysql')
    q = "SELECT title, url, insertdate, time, urlid FROM spider_info where insertdate>='%s 00:00' and insertdate <='%s 23:59' " % (insertdate, insertdate)
    if domain:
	q = q + " and url like '%" + domain + "%'"
    q = q + " order by urlid desc"
    q = q + " limit %s" % limit
    cur.execute(q)

    data = []
    urls = []
    metainfo = {}
    visited = ''
    for row in cur.fetchall():
        metadata = {}
        metadata['title'] = row[0]
        metadata['timestring'] = str(row[3])
	metadata['date'] = insertdate
        metadata['urlid'] = row[4]
	metadata['url'] = row[1]
 	metadata['domain'] = urlparse(metadata['url']).hostname
        visited = visited + ' ' + str(metadata['urlid']) + ', '
        metadata['insertdate'] = row[2].isoformat()
        urls.append(metadata)
    return urls
