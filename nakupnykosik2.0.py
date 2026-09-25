sklad={"jablko":(1.0, "ovocie", 2),"ananas":(1.3, "ovocie", 500), "mrkva":(0.2, "zelenina", 800), "kitkat":(0.8, "sladkosti", 300), "kinder":(1.5, "sladkosti", 400)}

kosik=[]

celkova_cena=0
while True:
    print("Co chcete pridat do kosika?")
    polozka = input()
    if polozka == "koniec":
        break


    if polozka in sklad.keys():
        cena, kategoria, kusy = sklad[polozka]

        if kusy > 0:
            kosik.append(polozka)
            cena,kategoria, kusy = sklad[polozka]
            celkova_cena += cena

        sklad[polozka] = (cena, kategoria, kusy - 1 if kusy - 1 >= 0 else 0)
        print(f"pridame do kosika {polozka} stoji {cena} eur")
        print(f"v sklade je {kusy} kusov")


for polozka in kosik:
            cena , kategoria , kusy = sklad[polozka]
            print(f"{polozka} stoji {cena} eur a je to {kategoria} a je ich {kusy} kusov")

for polozka in kosik:

      cena , kategoria , kusy = sklad[polozka]
      print(f"\nVáš nakup stoji {celkova_cena} €")

print("----------------------------------")

while True:
      print("Mate 10% kupon?")
      odpoved = input()
      if odpoved =="nie":
            break
      if odpoved =="ano":
            zlava= celkova_cena * 0.10
            celkova_cena -= zlava
            print("Super tu je vaša nová cena: (cena_kosik)€")
            break

    


