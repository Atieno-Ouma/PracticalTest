
from flask import Flask
from flask import render_template
import requests
import pandas as pd
from werkzeug.wrappers import json

auth = {
    "user": "admin",
    "password": "district"
}

app= Flask(__name__)
@app.route('/')
def index():

    data_elements_url = "https://play.dhis2.org/2.34.6/api/datasets"
    data = {'Begining Balance': '100',
            'Quantity Dispensed': '70',
            'Clossing Ballancs': '30'}
    data_json = simplejson.dumps(data)
    payload = {'json_payload': data_json}
    r = requests.post("http://localhost:8080", data=payload)

    def get_json(url, auth):
        user = auth['user'];
        password = auth['password']

        r = requests.get(url, auth=(user, password))
        return r.json()




