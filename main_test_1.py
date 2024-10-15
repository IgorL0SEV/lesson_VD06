from flask import Flask

app = Flask(__name__)
app.config['SECRET KEY'] = 'your_secret_key'

from app import routes

