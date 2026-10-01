rom Lib.re import sub

import steamlit as st
from datatime import datetime

st.set_page_config(page_title="Nakupny kosik", page_icon=":shopping_cart:", layout="wide")

if "kosik" not in st.session_state:
    st.session_state.kosik = []

st.markdown("<h1 style='text-align: center;'> Vitajte v obchode</h1>", unsafe_allow_html=True)

st.markdown("<p>|Jablko=1.0€| |Ananas=1.3€| |Mrkva=0.2€| |Kitkat=0.8€| |Kinder=1.5€|</p>", unsafe_allow_html=True)



sklad={"jablko":(1.0, "ovocie", 2),"ananas":(1.3, "ovocie", 500), "mrkva":(0.2, "zelenina", 800), "kitkat":(0.8, "sladkosti", 300), "kinder":(1.5, "sladkosti", 400)}

kosik=[]

#vypis skladu 
st.write("Vitajte v obchode")
st.write("Toto je nas sklad:")
st.write("----------------------------------------------------------------")
st.write("|Jablko=1.0€| "
"|Ananas=1.3€|"
"|Mrkva=0.2€| "
"|Kitkat=0.8€| "
"|Kinder=1.5€|")
st.write("----------------------------------------------------------------")
celkova_cena=0
#pridavanie do kosika
while True:
    st.write("Co chcete pridat do kosika?")
    polozka = st.text_input("Polozka:")
    if polozka == "koniec":
        break


    if polozka in sklad.keys():
        cena, kategoria, kusy = sklad[polozka]

        if kusy > 0:
            st.session_state.kosik.append(polozka)
            cena,kategoria, kusy = sklad[polozka]
            celkova_cena += cena
#odpocitanie kusov zo skladu
        sklad[polozka] = (cena, kategoria, kusy - 1 if kusy - 1 >= 0 else 0)
        st.write(f"pridame do kosika {polozka} stoji {cena} eur")
        st.write(f"v sklade je {kusy} kusov")

#vypisovanie kosika
for polozka in st.session_state.kosik:
            cena , kategoria , kusy = sklad[polozka]
            st.write(f"{polozka} stoji {cena} eur a je to {kategoria} a je ich {kusy} kusov")

for polozka in st.session_state.kosik:

      
   st.write("----------------------------------")
#zlava
def aplikuj_zlavu(celkova_cena):
      zlava = celkova_cena * 0.10
      nova_cena = celkova_cena - zlava
      return round(nova_cena, 2)
while True:
      st.write("Mate 10% kupon?")
      odpoved = st.text_input("Odpoved:")
      if odpoved =="nie":
            st.write(f"Na sklade je {kusy} kusov {polozka}")
            st.write(f"Váš nakup stál {celkova_cena} €")
            break
      if odpoved =="ano":
            celkova_cena = aplikuj_zlavu(celkova_cena)
            st.write(f"Super tu je vaša nová cena: {celkova_cena} €")
            st.write(f"Na sklade je {kusy} kusov {polozka}")
            break
