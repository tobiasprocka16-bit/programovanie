sklad={"jablko":(1.0, "ovocie", 2),"ananas":(1.3, "ovocie", 500), "mrkva":(0.2, "zelenina", 800), "kitkat":(0.8, "sladkosti", 300), "kinder":(1.5, "sladkosti", 400)}

kosik=[]

#vypis skladu 
print("Vitajte v obchode")
print("Toto je nas sklad:")
print("----------------------------------------------------------------")
print("|Jablko=1.0€| "
"|Ananas=1.3€|"
"|Mrkva=0.2€| "
"|Kitkat=0.8€| "
"|Kinder=1.5€|")
print("----------------------------------------------------------------")
celkova_cena=0
#pridavanie do kosika
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
#odpocitanie kusov zo skladu
        sklad[polozka] = (cena, kategoria, kusy - 1 if kusy - 1 >= 0 else 0)
        print(f"pridame do kosika {polozka} stoji {cena} eur")
        print(f"v sklade je {kusy} kusov")

#vypisovanie kosika
for polozka in kosik:
            cena , kategoria , kusy = sklad[polozka]
            print(f"{polozka} stoji {cena} eur a je to {kategoria} a je ich {kusy} kusov")

for polozka in kosik:

      
   print("----------------------------------")
#zlava
def aplikuj_zlavu(celkova_cena):
      zlava = celkova_cena * 0.10
      nova_cena = celkova_cena - zlava
      return round(nova_cena, 2)
while True:
      print("Mate 10% kupon?")
      odpoved = input()
      if odpoved =="nie":
            print(f"Na sklade je {kusy} kusov {polozka}")
            print(f"Váš nakup stál {celkova_cena} €")
            break
      if odpoved =="ano":
            celkova_cena = aplikuj_zlavu(celkova_cena)
            print(f"Super tu je vaša nová cena: {celkova_cena} €")
            print(f"Na sklade je {kusy} kusov {polozka}")
            break
