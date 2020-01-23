from flask import Flask, render_template
import requests, json
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

my_key = 'D8FJrAVDcE5RHJ29uwD5lRftLXMDO6Tw3iGnj19V'

payload = {
        'api_key': my_key,
        'start_date': '2017-03-09',
        'end_date': '2017-03-11' }

endpoint = 'https://api.nasa.gov/planetary/apod'

@app.route('/')
def main():
    try:
        r = requests.get(endpoint, params=payload)
        data = r.json()
    except:
        print('please try again')
    return render_template('home.html', data=data)
