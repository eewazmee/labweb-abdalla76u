from flask import Flask, render_template, request
from data_handling import photoPath_from_name

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

@app.route('/portrait')
def portrait():
    name = str(request.args.get('name'))
    path = photoPath_from_name(name=name)
    print(path)
    #return [path]
    return render_template('portrait.html', p=path)


if __name__=="__main__":
    app.run()