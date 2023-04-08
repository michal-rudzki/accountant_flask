import json

class VaultDB:
    
    def __init__(self, *args, **kwargs):
        self.db_file = args[0]
    
    def openFile(self):
        with open(self.db_file, mode='r', encoding='utf-8') as filedb:
            db = json.load(filedb)
        return db
        