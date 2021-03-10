from flask import flask
app = flask (__name__)

@app.route('/')
def Write():
    return '<img scr = LawLogo.png>'
    return '<h1>Welcome to our law firm!</h1>'

@app.route('/about')
def Write_About():
    return '<h1>About Page</h1>'

@app.route('/Contact')
def Write_Contact():
    return '<h1>Contact</h1>'