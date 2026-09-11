ovocie = ["jablko", "ananas"]
zelenina = ["mrkva"]
sladkosti = ["kitkat","kinder"]


nakupny_kosik = [("jablko", 2),
                 "ananas", "kikat", "mrkva", "kinder"]


print("Kolko veci chces kupit ?")
pocet = int(input())

while True:
    print("Co chcete pridat do kosika?")
    vstup = input()
    if vstup == "uz nic" or vstup == "koniec":
        break
    nakupny_kosik.append(vstup)

for polozka in nakupny_kosik:
    if polozka in ovocie:
        print(f"{polozka} je ovocie")
    elif polozka in zelenina:
        print(f"{polozka} je zelenina")
    elif polozka in sladkosti:
        print(f"{polozka} je sladkosti")
    else:
        print(f"{polozka} je nieco ine")
    
