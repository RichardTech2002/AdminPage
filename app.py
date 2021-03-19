"""This is the main flask app file""" # I just want to straight up steal this code
from flask import Flask, render_template
import names

app = Flask(__name__)

def generate_names(numberofnames):
    """Generate random names"""
    nlist = []
    for i in range(numberofnames):
        nlist.append(names.get_full_name())
        print(i)

    return nlist

namelist = generate_names(10)

app = Flask(__name__)

@app.route('/')
def index():
    """Render home page"""
    return render_template("index.html", namelist=namelist)
    
