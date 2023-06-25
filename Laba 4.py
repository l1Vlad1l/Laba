import requests
from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')


