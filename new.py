from flask import Flask, render_template,request,flash
import requests
import base64
import json
import uuid

app = Flask(__name__)
app.secret_key = "your-secret-key"
@app.route('/',)
def home():
    return render_template('/index.html',title = 'Home')

@app.route('/index.html',)
def index():
    return render_template('/index.html',title = 'Home')

@app.route('/calculator.html', methods = ['POST','GET'])
def calculator():
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
    return render_template('/calculator.html',var = var,title = 'Calculator')



@app.route('/directoryEnumeration.html')
def lay():
    var = requests.get('https://api.github.com/repos/thecyberjerry/DirFU/contents/dirFU.py')
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

    # var2 = str(uuid.uuid1())
    with open('static/emails.json') as json_file:
        data = json.load(json_file)
        temp = data["emails"]
        user = "{}".format(em)
        if user in data['emails']:
            flash('Your Email is already received, ThankYou!!, if you want to resubmit email than wait for a month we clear our database after every month')
        elif user =="":
            pass
        else:
            temp.append(user)
            flash("Your Email is submitted. We will try to contact you as soon as possible.")
    write_json(data)

    return render_template('/contact.html',title='Contact')
@app.errorhandler(404)
def invalid_route(e):
    return render_template('/404.html')

app.run(debug=True)
