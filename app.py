from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/lists')
def lists():
    return render_template("lists.html")

@app.route('/lists/<formation>/<year>')
def filieres(formation,year):
    return [formation, year]

@app.route('/lists/<formation>/<year>')
def fise1a_json():
    return {
        "username": "eewaazmee",
    }
    
