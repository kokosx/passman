from tinydb import TinyDB, Query

class PasswordManager:
    def __init__(self):
        self.db = TinyDB('baza.json')
        self.query = Query()

    def write(self, social, mail, login, password):
        if self.db.search(self.query.social.one_of(['social'])):
            print("EXISTS")
        else:
            self.db.insert({'social': social.lower(), 'mail': mail, 'login': login,'password': password} )
    def read(self, social):
        try:
            result = self.db.search(self.query.social == social)
            print(result[0].get('social'))
        except:
            print("NOT FOUND")
    def printAll(self):
        res = self.db.search(self.query.social.exists())

        if res == []:
            return 0
        for i,n in enumerate(res):
            print(f"{[i+1]}: {n.get('social').capitalize()}")
        return 1

    def delete(self, social):
        self.db.remove(self.query.social == social.lower())
