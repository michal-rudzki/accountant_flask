import json
from modules.myglobal import FILEDB

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
        
    def loadFile(self):
        pass
        
    def addItem(self, file_db, item, quantity):
        file_db['magazyn'].update({item: quantity})
        self.openFileToSave(file_db)
    
    def checkItem(self, item):
        pass
    
    def checkQuantity(self, quantity):
        pass
    
    def removeItem(self, item, quantity):
        pass