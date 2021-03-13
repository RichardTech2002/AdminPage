from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def Write():
    return render_template('FlaskTemplate.HTML')


"""@app.route('/about')
def Write_About():
    return '<h1>About Page</h1>'


@app.route('/Contact')
def Write_Contact():
    return '<h1>Contact</h1>'"""
