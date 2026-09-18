sklad={"jablko":(1.0, "ovocie", 1000),"ananas":(1.3, "ovocie", 500), "mrkva":(0.2, "zelenina", 800), "kitkat":(0.8, "sladkosti", 300), "kinder":(1.5, "sladkosti", 400)}

kosik=[]

celkova_cena=0
while True:
    print("Co chcete pridat do kosika?")
    polozka = input()
    if polozka == "koniec":
        break

    if polozka in sklad.keys():
        kkosik.append(polozka)
        cena,kategoria, kusy = sklad[polozka]
        celkova_cena += cena
        print(f"pridame do kosika{polozka} stoji {cena} eur")

    else:  
        print(f"{polozka} nie je v sklade")
        for polozka in kosik:
            cena,kategoria, kusy = sklad[polozka]
            print(f"{polozka} stoji {cena} eur a je to {kategoria} a je ich {kusy} kusov")
    


