#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import environ as env
from sys import argv

import bottle
from bottle import default_app, request, route, response, get, run
import settings
import re

@route('/:#.*#',method='ANY')
def index():
    path = request.path
    print(type(path))
    print(path)
    if "blog" in path:
        full_path = "{0}{1}".format(settings.BASE_NEW_PATH, path)
        return bottle.redirect(full_path, 301)
    else:
        print("Not a blog link")
        return bottle.redirect("{0}/blog/".format(settings.BASE_NEW_PATH), 301)

run(host='0.0.0.0', port=argv[1])