from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='../static', template_folder='../templates')

@app.route('/')
def index():
    return render_template('README.j2')

@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory('../static/images', filename)
