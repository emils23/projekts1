import math, sqlite3

conn = sqlite3.connect('vienadojumi.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS kvadratvienadojumi (NR INTEGER PRIMARY KEY AUTOINCREMENT, a REAL, b REAL, c REAL, diskriminants REAL, saknesIr TEXT, x1 REAL, x2 REAL)')


def kva():
    """
    funkcija aprēķina kvadrātvienādojuma
    a*x**2+b*x+c=0

    diskriminantu un, ja iespējams, saknes
    """
    a = float(input("Ievadi kvadrātvienādojuma koeficientu a"))
    b = float(input("Ievadi kvadrātvienādojuma koeficientu b"))
    c = float(input("Ievadi kvadrātvienādojuma koeficientu c"))
    
    d = b**2 - 4*a*c

    if d>0:
        x1 = (-b+math.sqrt(d))/(2*a)
        x2 = (-b-math.sqrt(d))/(2*a)
        print(f"Kvadrātvienādojuma diskriminants ir {d}, saknes \nx1 = {x1}\nx2={x2}")
        dbieraksts = (a, b, c, d, "ir", x1, x2)
        cur.execute('INSERT INTO kvadratvienadojumi (a, b, c, diskriminants, saknesIr, x1, x2) VALUES (?, ?, ?, ?, ?, ?, ?)',dbieraksts)
        conn.commit()

    elif d == 0:
        x = -b/(2*a)
        print(f"Kvadrātvienādojuma diskriminants ir 0, sakne x = {x}")
        dbieraksts = (a, b, c, d, "ir", x)
        cur.execute('INSERT INTO kvadratvienadojumi (a, b, c, diskriminants, saknesIr, x1) VALUES (?, ?, ?, ?, ?, ?)',dbieraksts)
        conn.commit()

    else:
        print(f"Kvadrātvienādojuma diskriminants ir {d}, sakņu nav.")
        dbieraksts = (a, b, c, d, "nav")
        cur.execute('INSERT INTO kvadratvienadojumi (a, b, c, diskriminants, saknesIr) VALUES (?, ?, ?, ?, ?)',dbieraksts)
        conn.commit()

    # Programma piedāvās apskatīt risinājumu vēsturi.
    # Šajā gadījumā visus vai tikai ar saknēm. Šī prasība arī nosaka vajadzību DB laukam saknesIr
    # Tātad divi SELECT vaicājumi. Pārbaudes darbā būs viens vai divi.

    izvele = int(input("Vai vēlies apskatīt iepriekšējos risinājumus? \n1 visus\n2 tikai ar saknēm\n3 beigt darbu un neko neskatīties"))
    if izvele == 1:
        cur.execute('SELECT * FROM kvadratvienadojumi')
        atbilde = cur.fetchall()

        for katrs in atbilde:
            print(katrs)

    elif izvele == 2:
        cur.execute('SELECT * FROM kvadratvienadojumi WHERE saknesIr = "ir"')
        atbilde = cur.fetchall()

        for katrs in atbilde:
            print(katrs)

    elif izvele == 3:
        conn.commit()
        cur.close()
        conn.close()

    else:
        print("Izskatās, ka nezini ko gribi. Būs jārēķina vēl.")
        kva()
