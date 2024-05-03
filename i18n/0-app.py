#!/usr/bin/env python3
''' module to learn i18n
'''
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    ''' returns index.html file
    '''
    return render_template('index.html')
