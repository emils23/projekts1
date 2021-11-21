import json
import sqlite3

conn = sqlite3.connect('krekli.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS krekli (Nr INTEGER PRIMARY KEY AUTOINCREMENT,veids TEXT, info TEXT, skaits INTEGER, Piegāde TEXT, summa REAL)')

# Šos mainīgos programma vairākkārt. Padomā, kāpēc tie vajadzīgi? 
izmaksas = {"T": 5, "Z": 7, "F": 20}
produktuNosaukumi = {"T": "teksts", "Z": "zīme", "F": "foto"}

with open("pasutijumi.json", "r", encoding='utf-8') as fails:
    dati = fails.read()

visiPasutijumi = json.loads(dati)

def navigacija():
    print("Ko darīt")
    print("1 – Pievienot pasūtījumu")
    print("2 – Meklēt pasūtījumu datus")
    print("3 – Rādīt visus pasūtījumus")
    print("4 – beigt darbu")

    izvele = int(input("Ko darīt?"))

    if izvele == 1:
        pievienot()
    elif izvele == 2:
        meklet()
    elif izvele == 3:
        visi()
    elif izvele == 4:
        beigt()
    else:
        print("Nesaprotama izvēle")
        navigacija()
    
def pievienot():
    veids = input("Kādu apdruku vēlies pasūtīt (T, Z, F)?")
    info = input("Norādi tekstu vai attēla datnes nosaukumu")
    skaits = int(input("Cik kreklus pasūtīsi?"))
    piegade = input("Vai vajag piegādi? j/n")

    sagatavot(veids, info, skaits, piegade)


def sagatavot(veids, info, skaits, piegade):    
    pasutijums = {}
        
    summa = izmaksas[veids] * skaits
    if summa > 100:
        summa = summa * 0.95
    
    if piegade == "j":
        summa += 7

    # ko dara nākamās piecas rindas? funkcija sarindo un numurē pasūtījumus
    if len(visiPasutijumi)>0:
        pedejaisNr = int(visiPasutijumi[-1]["Nr"])
        nr = pedejaisNr+1
    else:
        nr = 1

    pasutijums["Nr"] = nr
    pasutijums["veids"] = produktuNosaukumi[veids]
    pasutijums["info"] = info
    pasutijums["skaits"] = skaits
    pasutijums["summa"] = summa
    pasutijums["Piegāde"] = piegade

    jaunais = (veids, info, skaits, summa, piegade)
    c.execute('INSERT INTO krekli(veids, info, skaits, summa, Piegāde) VALUES (?, ?, ?, ?, ?)', jaunais)
    conn.commit()

    navigacija()

def visi():
    #for pasutijums in visiPasutijumi:
        #for atslega in pasutijums:
            #print(f'{atslega}: {pasutijums[atslega]}')
    #print()

    c.execute('SELECT * FROM krekli')
    rezultats = c.fetchall()
    print(rezultats)
    navigacija()

def meklet():

    kurMeklet = input("Kuros datos meklēt? (veids, info, piegāde)")
    # kas ir \n nākamajā rindā? n\ atdala jautājumus un ievada nākamajā
    koMeklet = input("Raksti meklējamo frāzi! \n teksts, zīme vai foto, lai meklētu veidu \n meklējamo tekstu vai faila nosaukuma fragmentu, lai meklētu satura info \n j vai n, lai meklētu piegādes info \n")
    kurMeklet = kurMeklet.capitalize()
    
    atrada = False
    for viens in visiPasutijumi:        
        if koMeklet in viens[kurMeklet]:
            print("Atrasts:")
            atrada = True
            for atslega in viens:
                print(f'{atslega}: {viens[atslega]}')
    if not atrada:
        print("Nekas nav atrasts\n")
    
    navigacija()     



def beigt():
    dati = json.dumps(visiPasutijumi, ensure_ascii=False)
    
    with open("pasutijumi.json", "w", encoding='utf-8') as fails:
        fails.write(dati)

    print("Darbs ar programmu pārtraukts")

    conn.commit()
    c.close()
    conn.close()


navigacija()

# Uzdevums 3. novembrī

# Programmai pievienot nepieciešamo kodu, kurā:

## tiktu izveidots savienojums ar datubāzi "krekluapdruka"
## būtu izveidots kursors. Nosaukums Tavā ziņā.
## izveidota tabula ar nepieciešamajiem laukiem atbilstoši JSON struktūrai. (Izveido vairākus
## pasūtījumus un beidz darbu, lai pārliecinātos par pareizajiem datu tipiem). Numura laukam jābūt primārajai atslēgai





