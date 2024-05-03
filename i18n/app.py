#!/usr/bin/env python3
''' module to learn i18n
'''
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
