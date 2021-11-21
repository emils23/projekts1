# importē nepieciešamo moduli darbam ar sqlite
import sqlite3

# izveido savienojumu ar datubāzi atkartojums.db (šādas DB nav, tāpēc Python to izveidos tukšu)
conn = sqlite3.connect('atkartojums.db')

# izveido kursoru ar mainīga nosaukumu “kur”
kur = conn.cursor()

# datubāzē uztaisa jaunu tabulu “macibas” ar laukiem
# ID (vesels skaitlis, primārā atslēga),
# macibuPrieksmets (teksts)
# stunduSkaits (vesels skaitlis)

kur.execute('CREATE TABLE IF NOT EXISTS macibas (ID INTEGER PRIMARY KEY, macibuPrieksmets TEXT, stunduSkaits INTEGER)')

# datubāzei pievieno divus ierakstus (var ar mainīgajiem + input, var arī vienkārši; kā sanāks, tā būs labi)

for i in range(2):
    prieksmets = input("kāds mācibu priekšmets?")
    skaits = int(input("Cik reizes nedēļā?"))
    jauns = (prieksmets, skaits)
    kur.execute('INSERT INTO macibas (macibuPrieksmets, stunduSkaits) VALUES (?, ?)', jauns)

# parāda visus tabulas macibas ierakstus
kur.execute('SELECT * FROM macibas')
rezultats = kur.fetchall()
print(rezultats)

# saglabā izmaiņas datubāzē, aizver kursora un datubāzes savienojumus
conn.commit()
kur.close()
conn.close()



