from flask import Flask
from flask import render_template
from flask import request

import json
import jinja2

from modules.myglobal import FILEDB
from modules.files_operation import VaultDB, Warehouse

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    title = "Witaj"
    db = Warehouse(FILEDB)
    file_db = db.openFileToRead()
    
    print(file_db['magazyn'])
    
    saldo = sum([int(s) for s in file_db['saldo'].keys()])
    magazyn = [(k, v) for k,v in file_db['magazyn'].items()]

    operation = request.form.get('accountent')
    name = request.form.get('name')
    quantity = request.form.get('quantity')
    prize = request.form.get('prize')

    if operation == 'purchase':
        print(operation, name, quantity, prize)
        db.addItem(file_db, name, int(quantity))
        magazyn.append((name, int(quantity)))
        return render_template('index.html', accountent=operation, title=title, saldo=saldo, magazyn=magazyn, name=name, quantity=quantity, prize=prize)
    
    if operation == 'sale':
        print(operation, name, quantity, prize)
        # pobrać name z file_db i sprawdzić ilość
        # return redirect(url_for('index', accountent=operation, title=title, saldo=saldo, magazyn=magazyn, name=name, quantity=quantity, prize=prize))
    
    return render_template('index.html', accountent=operation, title=title, saldo=saldo, magazyn=magazyn, name=name, quantity=quantity, prize=prize)

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
    
    return {'sukcess': True, 'msg:': f'Item: {item}, Quantity: {int(quantity)}'}

@app.route('/history/')
def history():
    title = 'History page'
    db = Warehouse(FILEDB)
    file_db = db.openFileToRead()
    history = file_db['historia']
    
    return render_template('history.html', title=title, history=history)

if __name__ == "__main__":
    app.config['JSON_AS_ASCII'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.auto_reload = True
    app.run(debug=True)