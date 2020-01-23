from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
import random

app = Flask(__name__)
bootstrap = Bootstrap(app)

images = {
        'Eastern':'static/img/34694102243_3370955cf9_z.jpg',
        'Beach':'static/img/34944112220_de5c2684e7_z.jpg',
        'Dessert':'static/img/35889114281_85553fed76_z.jpg',
        'Car':'static/img/36140096743_df8ef41874_z.jpg',
        'River':'static/img/36523127054_763afc5ed0_z.jpg',
        'Stairs':'static/img/36604481574_c9f5817172_z.jpg',
        'Windows':'static/img/36885467710_124f3d1e5d_z.jpg',
        'Wall':'static/img/36909037971_884bd535b1_z.jpg',
        'Tunnel':'static/img/37198655640_b64940bd52_z.jpg',
        'Library':'static/img/37246779151_f26641d17f_z.jpg'
}


@app.route('/', methods=['GET','POST'])
def index():
    rand_images = []
    while len(rand_images) != 3:
        title, source = random.choice( list(images.items()) )
        if([title,source] in rand_images):
            continue
        rand_images.append([title, source])
    #print(rand_images)
    link1 = '/' + rand_images[0][0].lower()
    link2 = '/' + rand_images[1][0].lower()
    link3 = '/' + rand_images[2][0].lower()
    return render_template('index.html', img = rand_images, link1 = link1, link2 = link2, link3 = link3)

@app.route('/eastern', methods=['GET','POST'])
def eastern():
    link = '/'+images['Eastern']
    return render_template('east.html', link = link)

@app.route('/beach', methods=['GET','POST'])
def beach():
    link = '/'+images['Beach']
    return render_template('beach.html', link = link)

@app.route('/dessert', methods=['GET','POST'])
def dessert():
    link = '/'+images['Dessert']
    return render_template('dessert.html', link = link)

@app.route('/car', methods=['GET','POST'])
def car():
    link = '/'+images['Car']
    return render_template('car.html', link = link)

@app.route('/river', methods=['GET','POST'])
def river():
    link = '/'+images['River']
    return render_template('river.html', link = link)

@app.route('/stairs', methods=['GET','POST'])
def stairs():
    link = '/'+images['Stairs']
    return render_template('stairs.html', link = link)

@app.route('/windows', methods=['GET','POST'])
def windows():
    link = '/'+images['Windows']
    return render_template('windows.html', link = link)

@app.route('/wall', methods=['GET','POST'])
def wall():
    link = '/'+images['Wall']
    return render_template('wall.html', link = link)

@app.route('/tunnel', methods=['GET','POST'])
def tunnel():
    link = '/'+images['Tunnel']
    return render_template('tunnel.html', link = link)

@app.route('/library', methods=['GET','POST'])
def library():
    link = '/'+images['Library']
    return render_template('lib.html', link = link)
