from flask import Flask, render_template,request
import requests
import base64
import re
import json
import uuid

app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def index():
    var = ''
    if request.method == 'POST' :

        if request.form.get('add') == 'ADD' and request.form.get('numberOne') and request.form.get('numberTwo'):
            no1= int(request.form.get('numberOne'))
            no2 = int(request.form.get('numberTwo'))
            var = no1+no2
        elif request.form.get('sub') == 'SUB':
            no1= int(request.form.get('numberOne'))
            no2 = int(request.form.get('numberTwo'))
            var = no1-no2
        elif request.form.get('mul') == 'MUL':
            no1= int(request.form.get('numberOne'))
            no2 = int(request.form.get('numberTwo'))
            var = no1*no2
        elif request.form.get('div') == 'DIV':
            no1= int(request.form.get('numberOne'))
            no2 = int(request.form.get('numberTwo'))
            var = no1/no2
        else:
            pass
    return render_template('/calculator.html',var = var)

@app.route('/index.html')
def home():
    return render_template('/index.html',title = 'Home')

@app.route('/calculator.html')
def calculator():
    return render_template('/calculator.html',title = 'Calculator')

@app.route('/directoryEnumeration.html')
def lay():
    var = requests.get('https://api.github.com/repos/thecyberjerry/Dirfu/contents/dirfu.py')
    data = var.json()
    file_content = data['content']
    file_content_encoding = data.get('encoding')
    if file_content_encoding == 'base64':
        file_content = base64.b64decode(file_content).decode()
    var2 = file_content
    return render_template('/directoryEnumeration.html',var = var2,title='DirectoryEnumeration')

@app.route('/contact.html',methods = ["POST","GET"])
def ema():
    em = ''
    if request.method == 'POST':

        if request.form.get('submit') and request.form.get('email'):
            em = request.form.get('email')
        else:
            pass

    def write_json(data):
        with open('static/emails.json', 'w') as file:
            json.dump(data, file, indent=4)
            pass

    var2 = str(uuid.uuid1())
    with open('static/emails.json') as json_file:
        data = json.load(json_file)
        temp = data["emails"]
        user = {"UID: ": "{}".format(var2),
                "email": "{}".format(em)}
        temp.append(user)
    write_json(data)
    return render_template('/contact.html', result=em)


@app.errorhandler(404)
def invalid_route(e):
    return render_template('/404.html')

app.run(debug=True)