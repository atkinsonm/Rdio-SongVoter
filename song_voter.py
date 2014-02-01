#!/usr/bin/python2

import json
from flask import Flask, render_template, request, url_for, redirect
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('songvoter.html')
    elif request.method == 'POST':
        #return json.dumps(search_for_song(request.form.get('lyrics',''))[0])

#@app.route('/play')
#def play():
    #print request.args
    #return render_template('play.html', trackData=request.args)

@app.route('/helper.html')
def helper():
    return render_template('helper.html')

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)