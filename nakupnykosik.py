produkty={"jablko":("ovocie"),"ananas":("ovocie"), "mrkva":("zelenina"), "kitkat":("sladkosti"), "kinder":("sladkosti")}


nakupny_kosik = [("jablko", 3),
                 ("ananas", 3),
                 ("kikat", 1),
                 ("mrkva", 2),
                 ("kinder", 1)]


print("Kolko veci chces kupit?")
pocet = int(input())


ceny = {"jablko": 0.5, "ananas": 1.3 , "mrkva": 0.2, "kitkat": 0.8, "kinder": 1.5} 



while True:
    print("Co chcete pridat do kosika?")
    vstup = input()
    if vstup == "uz nic" or vstup == "koniec":
        break
    nakupny_kosik.append(vstup)

for polozka in nakupny_kosik:
    if polozka in ceny:
        print(f"{polozka} stoji {ceny[polozka]} eur " )

    if polozka in produkty:
        print(f"{polozka} je {produkty[polozka]}")

for polozka in nakupny_kosik:
    if polozka in ovocie:
        print(f"{polozka} je ovocie")
    elif polozka in zelenina:
        print(f"{polozka} je zelenina")
    elif polozka in sladkosti:
        print(f"{polozka} je sladkosti")
    else:
        print(f"{polozka} je nieco ine")