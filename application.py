#!/usr/bin/env python3

"""
Title: Python Website
Author: Brandon Klett
Description:
    Python script using AWS LightSail and Flask to meet
the criteria set forth by HKN1 — HKN1 Task 2: Network Security

"""
from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
    return "<h1>Page is created to satisfy Task 2: Network Security</h1>"

if __name__ == "__main__":
    application.run(debug=False)