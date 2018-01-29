import sqlite3

from sqlalchemy import Column, Integer, String, NUMERIC
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Sequence

def createTestingDatabase(dbName):
    connection = sqlite3.connect(dbName)

    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS
    magazyn (id Integer Primary Key, name String, itemCount Integer)
    ''')

    cursor.execute('''
    INSERT INTO magazyn(id,name,itemCount) 
    SELECT 1, 'Mr Mercedes', 10
    WHERE NOT EXISTS(SELECT 1 FROM magazyn WHERE id = 1)
    ''')
    cursor.execute('''
    INSERT INTO magazyn(id,name,itemCount) 
    SELECT 2, 'Town of Salem', 20
    WHERE NOT EXISTS(SELECT 1 FROM magazyn WHERE id = 2)
    ''')
    cursor.execute('''
    INSERT INTO magazyn(id,name,itemCount) 
    SELECT 3, 'Dark Tower', 30
    WHERE NOT EXISTS(SELECT 1 FROM magazyn WHERE id = 3)
    ''')
    connection.commit()


    #for row in cursor.execute('SELECT * FROM magazyn'):
    #    print row

    connection.close()
#--------------------------------------------

class Database:
    engine = None
    session = None
    dbName = None
    def __init__(self, dbName):
        self.dbName = dbName
        self.createDatabase(self.dbName)
        self.engine = create_engine('sqlite:///' + dbName, echo=False) 
        Session = sessionmaker(bind=self.engine)
        self.session = Session() 
        
    def createDatabase(self, dbName):
        connection = sqlite3.connect(dbName)

        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS
        magazyn (id Integer Primary Key, name String, itemCount Integer)
        ''')
        connection.commit()
        
        connection.close()
    def printCatalog(self):
        print "Id | Name | Item Count"
        for poz in self.session.query(Pozycja).all():
            print poz.id,  '| ' + poz.name + ' |', poz.itemCount
            
    def dodajPozycje(self, nazwa, ilosc):
        found = False
        for poz in self.session.query(Pozycja).all():
            if nazwa == poz.name:
                found = True
        if not found:
            poz = Pozycja(name=nazwa, itemCount=ilosc)
            self.session.add(poz)
            self.session.commit()
    def usunPozycje(self, nazwa):
        for poz in self.session.query(Pozycja).all():
            if nazwa == poz.name:
                self.session.delete(poz)
    def zdejmijZeStanu(self,nazwa,ilosc):
        found = False
        for poz in self.session.query(Pozycja).all():
            if nazwa == poz.name and poz.itemCount > 0:
                poz.itemCount -= ilosc
                if poz.itemCount < 0:
                    poz.itemCount = 0
                self.session.commit()
    def dodajDoStanu(self,nazwa,ilosc):
        found = False
        for poz in self.session.query(Pozycja).all():
            if nazwa == poz.name:
                poz.itemCount += ilosc
                self.session.commit()


Base = declarative_base()
class Pozycja(Base):
    __tablename__ = 'magazyn'
    id = Column(Integer, Sequence('pozycja_id_seq'),  primary_key = True)
    name = Column(String(100))
    itemCount = Column(Integer)
    

dbName = 'magazyn.db'
#createTestingDatabase(dbName)
db = Database(dbName)

db.dodajPozycje('Dlugopis', 40)
db.dodajPozycje('Olowek', 40)
db.usunPozycje('Dlugopis')
db.zdejmijZeStanu('Olowek', 30)
db.dodajDoStanu('Olowek', 40)
db.dodajDoStanu('Olowek2', 40)
db.usunPozycje('Olowek2')
db.printCatalog()

