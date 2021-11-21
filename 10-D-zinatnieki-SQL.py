import sqlite3

conn = sqlite3.connect('zinatnieki-datubaze.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS zinatnieki (vārds TEXT, uzvārds TEXT, dzGads INTEGER, mGads INTEGER, valsts TEXT, joma TEXT, ID INTEGER PRIMARY KEY AUTOINCREMENT)')

def izvelne():
    print("Izvēlies ko darīsi")
    print("1: parādīt datus")
    print("2: pievienot jaunu ierakstu")
    print("3: meklēt pēc uzvārda")
    print("4: saglabāt un beigt darbu")
    izv = input("Ko izvēlējies? ")
    if izv == "1":
        radit()
    elif izv == "2":
        pievienot()
    elif izv == "3":
        meklet()
    elif izv == "4":
        beigas()
    else:
        print("Nesapratu. Vēlreiz.")
        izvelne()

def radit():
    c.execute('SELECT * FROM zinatnieki')
    rezultats = c.fetchall()

    for viens in rezultats:
        print(viens)

    izvelne()

def meklet():
    uzv = input("Raksti meklējamo uzvārdu! ")
    uzv = uzv.capitalize() # pirmais burts liels, pārejie mazi

    c.execute('SELECT * FROM zinatnieki WHERE uzvārds = ?',(uzv,))
    rezultats = c.fetchall()    

    if len(rezultats)>0:
        print(rezultats)
    else:
        print("Nekas nav atrasts\n")

    izvelne()     
    

def pievienot():
    vards = input("Raksti zinātnieka vārdu ")
    uzvards = input("Raksti zinātnieka uzvārdu ") 
    dzG = int(input("Raksti zinātnieka dzimšanas gadu "))
    mG = int(input("Raksti zinātnieka miršanas gadu "))
    valsts = input("Kurā valstī zinātnieks strādaja? ")
    joma = input("Kādā jomā zinātnieks strādāja? ")

    jaunsZin = (vards, uzvards, dzG, mG, valsts, joma)

    c.execute('INSERT INTO zinatnieki (vārds, uzvārds, dzGads, mGads, valsts, joma) VALUES (?, ?, ?, ?, ?, ?)',jaunsZin)

    conn.commit()

    print("\nIeraksts saglabāts datubāzē\n")
    izvelne()

def beigas():
    conn.commit()
    c.close()
    conn.close()
    print("Dati saglabāti datubāzē. Programma beidz darbu. \nUz redzēšanos!")

izvelne()