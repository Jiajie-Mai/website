import os

from flask import Flask, render_template, session, request, url_for, redirect, flash, jsonify

import json

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("website.html");

@app.rout('/me')

if __name__ == '__main__':
    app.run(debug=True)
