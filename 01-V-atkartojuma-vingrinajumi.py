def pirmais(cipars1, cipars2):
    return cipars1 + cipars2
    # pārveido funkciju, lai tai būtu divi skaitliski parametri
    
    # un pass vietā koda rinda, kura atgriež šo parametru summu


# Izveido funkciju otrais ar diviem skaitliskiem parametriem s1 un s2.
# Tajā ar print un f-string parādi šādas matemātiskas darbības ar s1 un s2 un darbību rezultātus:
# / // % ** divmod
# un pieraksti komentāru, ko katra no tām dara
def otrais(s1, s2):
    print (f"{s1}/{s2}={s1/s2},{s1//s2},{s1%s2},{s1**s2},{divmod,s1,s2}")
    

# Izveido funkciju tresais ar vienu skaitlisku parametru
# Funkcijai jāatgriež True, ja skaitlis ir 0 vai pozitīvs un False, ja negatīvs
def tresais(g1):
    if g1 >= 0:
        return True
    if g1 <= 0:
        return False
    
    

# Funkcijai ceturtais arī jābūt ar vienu skaitlisku parametru un
# jāatgriež True, ja skaitliskais parametrs ir vesels skaitlis
def ceturtais(sk):
    if sk//1==sk:
        return True

# Dots skaitļu masīvs
virkne = [1, 7, 5, 3]

# Izveido funkciju piektais bez parametriem.
# Funkcijai jāsakārto masīvs dilstošā secībā un jāparāda tā vērtības stabiņā uz leju
def piektais():
    virkne.sort(reverse=True)
    for skaitlis in virkne:
        print(skaitlis)
    

# Funkcija sestais jāveido ar vienu skaitlisku parametru s un tai noderēs piektās f-jas kods.
# Funkcijai jāparāda s dalījums kā vesels skaitlis ar katru masīva virknes elementu
# Kad tas ir izdevies, papildini funkciju, lai šie dalījumi tiktu sasummēti un summa beigās parādīta

def sestais(s):
    virkne.sort(reverse=True)
    summa=0
    for skaitlis in virkne:
        dalijums = s//skaitlis
        print(dalijums)
        summa += dalijums
    print(summa)

    
# Pēdējā, septītā būs līdzīga sestajai.
# Skaitliskais parametrs s joprojām jādala ar masīva virknes elementiem, un katrs dalījums jāatņem no sakotnējā s
# Tātad cikla nākamajā solī s jau būs mazāks.
# Tāpat kā sestajā f-jā, jāparāda katrs dalījums kā vesels skaitlis un beigās to, kas palicis pāri no sākotnējā s
def septītais(s):
    for skaitlis in virkne:
        dalijums = s//skaitlis
        print(dalijums)
        s -= dalijums
    print(s)
