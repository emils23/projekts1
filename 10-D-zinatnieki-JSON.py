import json

with open("zinatnieki-piemers.json", "r", encoding='utf-8') as fails:
    dati = fails.read()

zinatnieki = json.loads(dati)

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
    for z in zinatnieki:
        for atslega in z:
            print(f'{atslega}: {z[atslega]}')
        print()
    izvelne()

def meklet():
    uzv = input("Raksti meklējamo uzvārdu! ")
    uzv = uzv.capitalize() # pirmais burts liels, pārejie mazi
    atrada = False
    for z in zinatnieki:        
        if uzv in z["uzvārds"]:
            print("Atrasts:")
            atrada = True
            for atslega in z:
                print(f'{atslega}: {z[atslega]}')
    if not atrada:
        print("Nekas nav atrasts\n")
    izvelne()     
    

def pievienot():
    zin = {}    
    vards = input("Raksti zinātnieka vārdu ")
    uzvards = input("Raksti zinātnieka uzvārdu ") 
    dzG = int(input("Raksti zinātnieka dzimšanas gadu "))
    mG = int(input("Raksti zinātnieka miršanas gadu "))
    valsts = input("Kurā valstī zinātnieks strādaja? ")
    joma = input("Kādā jomā zinātnieks strādāja? ")

    zin["vārds"] = vards
    zin["uzvārds"] = uzvards
    zin["dzGads"] = dzG
    zin["mGads"] = mG
    zin["valsts"] = valsts
    zin["joma"] = joma

    zinatnieki.append(zin)
    print("\nDati saglabāti masīvā\n")
    izvelne()

def beigas():
    dati = json.dumps(zinatnieki, ensure_ascii=False)
    
    with open("zinatnieki-piemers.json", "w", encoding='utf-8') as fails:
        fails.write(dati)

    print("Dati saglabāti failā. Programma beidz darbu. \nUz redzēšanos!")

izvelne()
