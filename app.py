from flask import Flask
from flask import render_template
from flask import request

import json
import jinja2

from modules.myglobal import FILEDB
from modules.files_operation import VaultDB

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    title = "Witaj"
    db = VaultDB(FILEDB)
    file_db = db.openFile()
    saldo = sum([int(s) for s in file_db['saldo'].keys()])

    operation = request.form.get('accountent')
    name = request.form.get('name')
    quantity = request.form.get('quantity')
    prize = request.form.get('prize')
    
    return render_template('index.html', title=title, db=db, saldo=saldo)

@app.route('/history/')
def history():
    title = 'History page'
    db = VaultDB(FILEDB)
    file_db = db.openFile()
    history = file_db['historia']
    
    return render_template('history.html', title=title, history=history)

if __name__ == "__main__":
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True)