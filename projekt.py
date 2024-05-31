# Importování modulu clear_output z IPython.display
from IPython.display import clear_output
import random
import time

# Funkce pro postupné zobrazování textu
def zobrazit_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)

# Úvodní zpráva
text1 = "\n Vítejte v Piškvorkách!".upper()                                                                                                  
zobrazit_text(text1)

while True:
    time.sleep(1)
    print("")
    spusteni_hry = input("\n Pro start zmáčkněte enter: ")
    if spusteni_hry == "":
        break
    else:
        print("\n Neplatný vstup. Zmáčkněte pouze enter.")
    
time.sleep(1)

def zobrazit_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)

text2 = "\n Tutoriál:".upper() 
zobrazit_text(text2)

time.sleep(1)

# Funkce pro zobrazení hrací desky
def zobrazit_desku(deska):
    print("\n")    
    print("   |   |")
    print(" " + deska[7] + " | " + deska[8] + " | " + deska[9])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + deska[4] + " | " + deska[5] + " | " + deska[6])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + deska[1] + " | " + deska[2] + " | " + deska[3])
    print("   |   |")

# Testovací hrací deska
testovaci_deska = ["#", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
zobrazit_desku(testovaci_deska)

time.sleep(2)

def zobrazit_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)

text3 = ("\n Můžete vidět, že čísla jsou v hracím poli umístěna stejně jako na klávesnici.")
zobrazit_text(text3)

def zobrazit_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)

print("")
text4 = ("\n Ve hře zmáčkněte na klávesnici libovolné číslo 1-9 a symbol se zobrazí na dané pozici.")
zobrazit_text(text4)

time.sleep(2)

# Funkce pro vstup hráče
def vstup_hrace():
    print("")
    hrac1 = input("\n Zadejte jméno prvního hráče: ")
    hrac2 = input("\n Zadejte jméno druhého hráče: ")
    
    znacka = " "
    
    while not (znacka == "X" or znacka == "O"):
        znacka = input(f"\n {hrac1}?: Chcete hrát jako X nebo O? ")

    if znacka == "X":
        return (hrac1, "X", hrac2, "O")
    else:
        return (hrac1, "O", hrac2, "X")

# Funkce pro kontrolu výhry
def kontrola_vyhry(deska, znacka):
    return ((deska[7] == znacka and deska[8] == znacka and deska[9] == znacka) or  # přes vrchol
            (deska[4] == znacka and deska[5] == znacka and deska[6] == znacka) or  # přes střed
            (deska[1] == znacka and deska[2] == znacka and deska[3] == znacka) or  # přes spodek
            (deska[7] == znacka and deska[4] == znacka and deska[1] == znacka) or  # dolů po levé straně
            (deska[8] == znacka and deska[5] == znacka and deska[2] == znacka) or  # dolů po středu
            (deska[9] == znacka and deska[6] == znacka and deska[3] == znacka) or  # dolů po pravé straně
            (deska[7] == znacka and deska[5] == znacka and deska[3] == znacka) or  # diagonálně
            (deska[9] == znacka and deska[5] == znacka and deska[1] == znacka))  # diagonálně

# Funkce pro umístění značky na desku
def umistit_znacku(deska, znacka, pozice):
    deska[pozice] = znacka

# Funkce pro volbu, kdo začne jako první
def volba_prvniho(hrac1, hrac2):
    if random.randint(0, 1) == 0:
        return hrac1
    else:
        return hrac2

# Funkce pro kontrolu, zda je pozice volná
def kontrola_pozice(deska, pozice):
    return deska[pozice] == " " 

# Funkce pro kontrolu, zda je celá deska zaplněná
def kontrola_plne_desky(deska):
    for i in range(1, 10):
        if kontrola_pozice(deska, i):
            return False
    return True

# Funkce pro získání volby hráče
def volba_hrace(deska):
    pozice = 0
    
    while pozice not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not kontrola_pozice(deska, pozice):
        time.sleep(1)
        pozice = int(input("\n Zvolte svou další pozici: (1-9) "))
        
    return pozice

# Funkce pro opakování hry
def znovu_hrat():
    while True:
        odpoved = input("\n Chcete hrát znovu? Zadejte Ano nebo Ne: ").strip().lower()
        if odpoved in ["ano", "ne"]:
            return odpoved == "ano"
        else:
            print("Neplatný vstup. Zadejte prosím 'Ano' nebo 'Ne'.")


while True:
    # Resetování desky
    deska = [' '] * 10
    hrac1, znacka_hrace1, hrac2, znacka_hrace2 = vstup_hrace()
    tah = volba_prvniho(hrac1, hrac2)
    print(f"\n {tah} začne jako první.")
    hrat_hru = input("\n Jste připraveni hrát? Zadejte Ano nebo Ne: ")
    
    time.sleep(1)
    
    if hrat_hru.lower()[0] == "a":
        hra_bezi = True
    else:
        hra_bezi = False

    while hra_bezi:
        if tah == "Hráč 1":
            # Tah hráče 1
            zobrazit_desku(deska)
            pozice = volba_hrace(deska)
            umistit_znacku(deska, znacka_hrace1, pozice)

            if kontrola_vyhry(deska, znacka_hrace1):
                zobrazit_desku(deska)
                print(f"\n Gratulujeme, {hrac1}!")
                print("\n Vyhráváte!")
                hra_bezi = False
            else:
                if kontrola_plne_desky(deska):
                    zobrazit_desku(deska)
                    print("\n Hra skončila remízou!")
                    break
                else:
                    tah = "Hráč 2"
        else:
            # Tah hráče 2
            zobrazit_desku(deska)
            pozice = volba_hrace(deska)
            umistit_znacku(deska, znacka_hrace2, pozice)

            if kontrola_vyhry(deska, znacka_hrace2):
                zobrazit_desku(deska)
                print(f"\n Gratulujeme, {hrac2}!")
                print("\n Vyhráváte!")
                hra_bezi = False
            else:
                if kontrola_plne_desky(deska):
                    zobrazit_desku(deska)
                    print("\n Hra skončila remízou!")
                    break
                else:
                    tah = "Hráč 1"

    if not znovu_hrat():
        break