# Jāizveido programmatūra bankomātam — ievadot vēlamo summu, saņemam banknotes.
# Tā kā banknošu veidošana mājās ir visnotaļ nepieņemama aktivitāte, programmai jāparāda tikai
# izsniedzamo banknošu skaitu, ja tas vispār ir iespējams, un tā, lai tās būtu pēc iespējas mazāk. Piemēram,
#

# banka(40)
# 20 EUR, 2 gab.
#
# banka(20)
# 20 EUR, 1 gab.
#
# banka(50)
# 20 EUR, 2 gab.
# 10 EUR, 1 gab.
#
# banka(21)
# šādu summu nevar izsniegt
#
banknotes = [5, 10, 20, 50, 100, 200, 500]

def bankomats(summa,banknotes):
    banknotes.sort(reverse = True)
    if summa%5 != 0:
        print("šādu summu nevar izsniegt")
    else:
        for nominals in banknotes:
            skaits = summa//nominals
            izsniegts = skaits*nominals
            summa -= izsniegts
            if skaits != 0:
                print(f"{nominals} EUR, {skaits} gab. ")
        
            
        
# Bet ir vēl viena problēma — ne visas bankas uzpilda visu nominālu banknotes, piemēram,
# 5 EUR banknotes nav pieejamas visos bankomātos.
# Tāpēc veidojot programmu, funkcijā kā parametru jāiedod arī masīvu ar pieejamajiem bankonšu nomināliem.
# Dzīvē tā nav, bet pieņemsim, ka nauda bankomātā pieejama bezgalīgā daudzumā.
#
# Tātad jāizveido funkcija bankomats ar 2 parametriem, no kuriem pirmais ir vesels skaitlis — naudas summa, ko vēlamies izņemt,
# otrais masīvs ar veseliem skaitļiem – pieejamajām vērtībām, piemēram — bankomats(summa, nominali) un izsauksim to bankomats(20, [5, 10, 20, 100])
# Tas, kā programma parādīs rezultātu, ir Tavā ziņā. Vari, kā šajos piemēros, vari kā citādi.

# Daži piemēri kontrolei
# bankomats(120, [10, 20, 50])
# 50 EUR, 2 gab.
# 20 EUR, 1 gab.
#
# bankomats(120, [5, 10, 50])
# 50 EUR, 2 gab.
# 10 EUR, 2 gab.

# Papilduzdevums. Funkcijai pievienot parametru maziNominali kurš ir bool tipa. Ja tas, izsaucot funkciju, ir True,
# tad nauda tiks izmaksāta vienā vai divos mazākajos pieejamajos nominālos.
# Piemēram,
#
# bankomats(100, [10, 20, 50], False)
# 50 EUR, 2 gab.
# 
# bankomats(100, [10, 20, 50], True)
# 20 EUR, 5 gab. # Šis jau būtu pietiekami, bet var apdomāt arī, kā dabūt smalkāku dalījumu:
#
# 20 EUR, 4 gab.
# 10 EUR, 2 gab.
