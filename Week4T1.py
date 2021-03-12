from flask import Flask
app = Flask(__name__)


@app.route('/')
def Write():
    return '<!DOCTYPE HTML>\
        <html>\
            <body>\
                <h1>Welcome to our law firm!</h1>\
                <img scr = Law_Logo.png>\
            </body>\
        </html>'


"""@app.route('/about')
def Write_About():
    return '<h1>About Page</h1>'


@app.route('/Contact')
def Write_Contact():
    return '<h1>Contact</h1>'"""
