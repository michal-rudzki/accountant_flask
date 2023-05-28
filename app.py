from flask import Flask
from flask import render_template
from flask import request

import json
import jinja2

from modules.myglobal import FILEDB
from modules.files_operation import VaultDB, Warehouse

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    title = "Witaj"
    #db = VaultDB(FILEDB)
    #file_db = db.openFile()
    db = Warehouse(FILEDB)
    file_db = db.openFileToRead()
    
    saldo = sum([int(s) for s in file_db['saldo'].keys()])
    magazyn = [(k, v) for k,v in file_db['magazyn'].items()]

    operation = request.form.get('accountent')
    name = request.form.get('name')
    quantity = request.form.get('quantity')
    prize = request.form.get('prize')
    
    return render_template('index.html', title=title, db=db, file_db=file_db, saldo=saldo, magazyn=magazyn)

@app.route('/zakup/', methods=['GET', 'POST'])
def zakup():
    db = Warehouse(FILEDB)
    file_db = db.openFileToRead()
    
    item = request.args.get('item')
    quantity = request.args.get('quantity')
    
    if not item:
        return {'sukces': False, 'msg': 'Nie podano nazwy dla przedmiotu'}
    
    try:
        quantity = float(quantity)
    except ValueError:
        return {'sukces': False, 'msg': 'Liczba sztuk musi być podana jako rzeczywista z kropką'}
    
    db.addItem(file_db, item, quantity)
    
    return {'sukcess': True, 'msg:': f'Item: {item}, Quantity: {quantity}'}

@app.route('/history/')
def history():
    title = 'History page'
    db = Warehouse(FILEDB)
    file_db = db.openFileToRead()
    history = file_db['historia']
    
    return render_template('history.html', title=title, history=history)

if __name__ == "__main__":
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True)