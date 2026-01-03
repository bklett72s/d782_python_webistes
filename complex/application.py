#!/usr/bin/env python3

"""
Title: Python Website
Author: Brandon Klett
Description:
    Python script using AWS LightSail and Flask to meet
the criteria set forth by HKN1 — HKN1 Task 2: Network Security

"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') # Renders the index.html file

@app.route('/about')
def about_page():
    return render_template('other_pages/about.html')
    
if __name__ == "__main__":
    app.run(debug=True)