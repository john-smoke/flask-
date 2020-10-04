from app import app
from flask import render_template
from random import randint
num = 0



    
    
@app.route('/')
@app.route('/index')
def index():
    global num
    query = randint(1,1000)
    num += 1
    imagenum1 = 'static/images/image1/image' + str(num) + '.gif'
    imagenum2 = 'static/images/image2/image' + str(num) + '.gif'
    imagenum3 = 'static/images/image3/image' + str(num) + '.gif'
    imagenum4 = 'static/images/image4/image' + str(num) + '.gif'
    imagenum5 = 'static/images/image5/image' + str(num) + '.gif'
    return render_template('main.html',query = query, num = num, imagenum1 = imagenum1, imagenum2 = imagenum2, imagenum3 = imagenum3, imagenum4 = imagenum4, imagenum5 = imagenum5)