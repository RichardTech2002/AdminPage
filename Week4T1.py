from flask import flask
app = flask (__name__)

@app.route('/')
def Write():
    return 'Hello, World!'