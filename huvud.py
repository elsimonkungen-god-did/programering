import random
from Svärd import *
from Spelare import *
import time

# funktioner

def om_monster(Karaktär):
    print("Du hittade ett monster")
    time.sleep(3)
    monster_styrka = random.randint(5, 30)
    if Karaktär.total_styrka() > monster_styrka:
        Karaktär.nivå += 1
        print("Du vann din strid mot monstret och ökade din nivå \n"
            f"Din level är nu {Karaktär.nivå}")
    elif Karaktär.total_styrka == monster_styrka:
        print("I din strid mot monstret blev det lika.\n"
            "Du tog ingen skada")
    else:
        Karaktär.liv -= 1
        print("Du förlorade din strid mot monstret och förlorade 1 liv\n"
            f"Ditt liv är nu {Karaktär.liv}")

def om_kista(Karaktär):
    svärd_styrka = random.randint(1, 3)
    while True:
        b = input(f"Du hittade ett svärd med styrkan {svärd_styrka} om du vill lägga in svärdet i ryggsäcken tryck 1 annars tryck 2 \n")
        if str(b) == "2":
            break
        if str(b) =="1":
            svärd_namn = input("Skriv vad du vill att svärdet ska heta \n")
            svärd_namn = Svärd(svärd_namn, svärd_styrka)
            #Här kollas om det finns max antal svärd
            if len(Karaktär.grejer) < 5:
                Karaktär.grejer.append(svärd_namn)
                return
            else:
                print("din ryggsäck är full\n"
                    "Om du vill lägga något i din ryggsäck måste du ta bort ett annat svärd")
                print("Det här är din ryggsäck \n")
                Karaktär.visa_rygga()
                while True:
                    x=input("Om du vill ta bort ett svärd och sedan lägga till ditt svärd skriv in numret på svärd du ska ta bort. \nAnnars skriv q \n \n")
                    if x == "q":
                        return
                    if (x == "1" or "2" or "3" or "4" or "5"):
                        x=int(x)
                        x = x-1
                        Karaktär.grejer.pop(x)
                        Karaktär.grejer.append(svärd_namn)
                        return


def main():
    print("\n Spelet går ut på att nå nivå 10. Man förlorar när man har 0 liv."
        "O man vinner en strid mot ett monster går man upp i en nivå om man förlorar förlorar man ett liv. \n"
        "Oavsett vilken karaktär du väljer är du en svärdsmästare som max kan slåss med 5 svärd samtidigt.")
    #Här är evighetsloop som kommer brytas när önskvärt svar skrivs in.
    while True:
        val =input("""
                                0            1       2       3           
        Typ                     Simon(gud) riddare  barbar lönnmördare
        Liv                     100         50      30      25
        Styrka                  100         8       10      15
        Svårighetsgrad          guide      enkel   medel   omöjlig    
        
        Skriv 0, 1, 2 eller 3
        """)
        if val == "0":
            Karaktär = Spelare(100,100, "simon")
            break
        if val == "1":
            Karaktär = Spelare(50,8, "riddare")
            break
        if val == "2":
            Karaktär = Spelare(35,10, "barbar")
            break
        if val == "3":
            Karaktär = Spelare(25,15, "lönnmördare")
            break
    #Evighets loop som bryts vid önskvärt svar
    while True:
        y = input("\nOm du vill se din statistik tryck 1.\nOm du vill se din ryggsäck tryck 2.\nOm du vill gå in genom en dörr tryck 3. \n")
        
        if y == "1":
            print(Karaktär)
        elif y == "2":
            Karaktär.visa_rygga()
        elif y == "3":
            #Variabeln svar behövs skapas in jag startar loopen.
            svar = ""
            #Koden bryts när svar finns i listan.
            while svar not in  ["H", "V", "F","h","v","f"]:
                svar = input("\nOm du vill ta dörren till höger tryck H, vänster V,framåt F \n")
            #Här bestäms det vad det är bakom dörren.
            bakom_dörr = random.randint(0, 2)
            if bakom_dörr == 1:
               om_monster(Karaktär)
            elif bakom_dörr == 2:
                print("\nDu hittade en kista!!,")
                om_kista(Karaktär)
            else:
                Karaktär.om_fälla()
            #Vid slutet av main loopen kollas det om spelet är slut.
            if Karaktär.nivå == 10:
                print("du är nivå 10 och har därför vunnit spelet ")
                break
            if Karaktär.liv == 0:
                print("Du har 0 liv och har därför förlorat")
                break


main()
