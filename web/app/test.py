#!/usr/bin/python

from newsdb import get_news

test = 'on'
if test:
    insdate = "2017-11-05"
    limit = 10
    domain = ''

    info = get_news(insdate, limit, domain)

    data = {}
    data['principles'] = info
    print str(info)
