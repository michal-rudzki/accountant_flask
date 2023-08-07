import json
from datetime import datetime
from modules.myglobal import FILEDB, DATE_FORMAT

class VaultDB:
    
    def __init__(self, *args, **kwargs):
        self.db_file = args[1]
    
    def openFileToRead(self):
        with open(self.db_file, mode='r', encoding='utf-8') as filedb:
            db = json.load(filedb)
        return db
    
    def openFileToSave(self, db):
        with open(self.db_file, mode='w', encoding='utf-8') as filedb:
            json.dump(db, filedb, ensure_ascii=False, indent=4)

class Warehouse(VaultDB):
    
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        
    def setDate(self):
        dateTime = datetime.now()
        """https://strftime.org/"""
        formattedTime = dateTime.strftime(DATE_FORMAT)
        return formattedTime
    
    def setSaldo(self, file_db, new_saldo):
        file_db['saldo'] = {self.setDate(): [int(new_saldo), "zerowanie salda - próba oszustwa"]}
        self.openFileToSave(file_db)
        
    def loadFile(self):
        pass
        
    def checkItem(self, file_db, item):
        """ checking an item if it's already in the 'magazyn' """
        if item in list(file_db['magazyn'].keys()):
            return True
        return False
    
    def addItemToWarehouse(self, file_db, item, quantity):
        if self.checkItem(file_db, item) is True:
            file_db['magazyn'][item] += quantity
        else: 
            file_db['magazyn'].update({item: quantity})
        #self.updatePurchase(file_db, item, prize, quantity) 
        self.openFileToSave(file_db)
        return file_db['magazyn']
    
    def updateHistory(self, file_db, operation, item, prize, quantity):
        correctTime = self.setDate()
        file_db['historia'].update({correctTime: {operation: {item: [float(prize), int(quantity)]}}})
        self.openFileToSave(file_db)
        
    def updatePurchase(self, file_db, item, prize, quantity):
        correctTime = self.setDate()
        file_db['sprzedaż'].update({correctTime: {item: [quantity, prize]}})
        self.openFileToSave(file_db)
    
    def checkQuantity(self, quantity):
        pass
    
    def removeItem(self, item, quantity):
        pass
    
class SaldoOperations(VaultDB):
    
    def __init__(self, *args, **kwargs):
        pass
    
    def set_saldo(self):
        pass
    
    def update_saldo(self):
        pass