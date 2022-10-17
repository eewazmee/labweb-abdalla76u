from flask import Flask
from flask import g

import sqlite3

DATABASE = 'static/data/trombi.db' # le nom du fichier de votre base sqlite3

app = Flask(__name__)

def get_db(): # cette fonction permet de créer une connexion à la base 
              # ou de récupérer la connexion existante 
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):  # pour fermer la connexion proprement
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    return 'TelecomBook is running!'


@app.route('/students')
def all_students():
    c = get_db().cursor() # on crée un curseur
    c.execute("select name, photo from students") # on exécute la requête

    content = '<b>Students</b>' 

    content += '<ul>'
    for tpl in c.fetchall(): # on parcours les tuples résultat 1 par 1
        content += f'<li>{tpl[0]} -> {tpl[1]}</li>'
    content += '</ul>'
    
    return content

if __name__=="__main__":
    app.run(debug=True)