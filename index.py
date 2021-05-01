#!/usr/local/bin/python3
# coding: utf-8

# from deepzoom_multiserver import app
from wsgiref.handlers import CGIHandler
import cgitb
cgitb.enable()

CGIHandler().run(app)
