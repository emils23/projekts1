# Lai Python strādātu ar sqlite
import sqlite3

# Izveido savienojumu ar DB
conn = sqlite3.connect('06-worldDB.sqlite')

# Kursors
# https://en.wikipedia.org/wiki/Cursor_(databases)
c = conn.cursor()


def demoA():
    # Vienkārša vaicājuma izsaukšana
    c.execute('SELECT * FROM city WHERE CountryCode = "LVA"')

    # "Noķert" vaicājuma rezultātu
    rezultats = c.fetchall()
    print(rezultats)
    # Print vienmēr nemaz nav vajadzīgs
    # Kas par mainīgo ir rezultāts?
    for rinda in rezultats:
        print(rinda)

        print(rinda[0])
        print(rinda[1])
        print(rinda[2])

        for lauks in rinda:
            print(lauks)
        



def demoB():

    # Kāds no labošanas vaicājumiem
    c.execute('INSERT INTO city (Name, CountryCode, District, Population) VALUES ("Valmiera", "LVA","Valmiera", 53000)' )

    # Paskatāmies, vai sanāca
    c.execute('SELECT * FROM city WHERE CountryCode = "LVA"')
    rezultats = c.fetchall()
    print(rezultats)

def demoC():
    # Kā ielikt mainīgo?
    jauns = ("Daugavpils", "LVA","Daugavpils", 77000)
    c.execute('INSERT INTO city (Name, CountryCode, District, Population) VALUES (?, ?, ?, ?)',jauns)
    # Tas pats ar f-string
    # c.execute(f'INSERT INTO city (Name, CountryCode, District, Population) VALUES {jauns}')

    # Paskatāmies, vai sanāca
    c.execute('SELECT * FROM city WHERE CountryCode = "LVA"')
    rezultats = c.fetchall()
    print(rezultats)

def demoD():    

    # Meklēšana DB -- select pēc "kaut kā", ko izvēlējās lietotājs.
    valsts = input("Uzraksti valsts kodu, kuru meklēt")
    c.execute('SELECT * FROM city WHERE CountryCode = ?',(valsts,))
    rezultats = c.fetchall()
    print(rezultats)

    # Sarežģītāks meklēšanas piemērs
    lauks = input("Pēc kā meklēt? (Name, CountryCode, District, Population)")
    ieraksts = input("Ko meklēt?")

    c.execute(f'SELECT * FROM city WHERE {lauks} = ?',(ieraksts,))
    rezultats = c.fetchall()
    print(rezultats)

def demoE():    
    # Un tagad pievienošana no ievades
    nosaukums = input("Raksti pilsētas nosaukumu")
    valstsKods = input("Raksti valsts kodu")
    regions = input("Raksti reģiona nosaukumu")
    iedzSk = int(input("Raksti iedzīvotāju skaitu"))
    saglabasanai = (nosaukums, valstsKods, regions, iedzSk)

    c.execute('INSERT INTO city (Name, CountryCode, District, Population) VALUES (?, ?, ?, ?)',saglabasanai)

    c.execute('SELECT * FROM city ORDER BY ID DESC LIMIT 5')
    rezultats = c.fetchall()
    print(rezultats)

def demoF():
    # Uztaisa jaunu tabulu
    c.execute('CREATE TABLE IF NOT EXISTS Celojumi (ID INTEGER PRIMARY KEY AUTOINCREMENT, Valsts TEXT, Gads INTEGER, Izmaksas INTEGER, BrauksuVel TEXT)')


def demoG():
    # Saglabājam izmaiņas datubāzē
    conn.commit()


    # Savienojuma ar DB aizvēršana
    c.close()
    conn.close()
        

# Dabūt lauku nosaukumus. Varbūt, ka vispār nevajadzēs.
# print(c.description)
# lauki = [description[0] for description in c.description]
# print(lauki)

# https://www.w3resource.com/python-exercises/sqlite/index.php

# 3., 4., 5., 6.
# 8., 12., 13.


