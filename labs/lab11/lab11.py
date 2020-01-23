# from flask import Flask, render_template
# app = Flask(__name__)
#
#
# @app.route('/hello')
# def hello():
#     return render_template('home.html',
#                             color = {
#                             "red":[(255,0,0), '#ff0000'],
#                             "green":[(0,255,0), '#00ff00'],
#                             "blue":[(0,0,255), '#0000ff']
#                             }
#                             )
######################### HELLO WORLD ################################
from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap(app)

class Playlist(FlaskForm):
    song_title = StringField('Song Title', validators=[DataRequired()])
    artist_name = StringField('Artist Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

playlist = []
artists = []

def store_song(my_song):
    playlist.append(dict(
        song = my_song,
        date = datetime.today()
    ))

def store_artist(my_artist):
    artists.append(dict(
        artist = my_artist
    ))

@app.route('/', methods=['GET','POST'])
def index():
    form = Playlist()
    if form.validate_on_submit():
        store_song(form.song_title.data)
        print(playlist)
        store_artist(form.artist_name.data)
        print(artists)
        return redirect('/pl')

    return render_template('index.html', form=form)

@app.route('/pl')
def pl():
    return render_template('pl.html', playlist=playlist, artists=artists)
