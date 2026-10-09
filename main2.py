import copy
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

app = FastAPI(title="Obchod")

# názov: (cena, kategória, kusy)
SKLAD_POVODNY = {
    "jablko": (1.0, "ovocie", 2),
    "ananas": (1.3, "ovocie", 500),
    "mrkva": (0.2, "zelenina", 800),
    "kitkat": (0.8, "sladkosti", 300),
    "kinder": (1.5, "sladkosti", 400),  # hlavný kód
}

sklad = copy.deepcopy(SKLAD_POVODNY)
kosik = []
stav = {"zlava": False}


class PridanieKusov(BaseModel):
    pocet: int = Field(gt=0, le=100_000)


def aplikuj_zlavu(celkova_cena):
    zlava = celkova_cena * 0.10
    nova_cena = celkova_cena - zlava
    return round(nova_cena, 2)


def spocitaj_cenu():
    cena = sum(sklad[p][0] for p in kosik)
    if stav["zlava"]:
        cena = aplikuj_zlavu(cena)
    return round(cena, 2)


def vypis_kosika():
    polozky = []
    for nazov in dict.fromkeys(kosik):
        cena, kategoria, kusy = sklad[nazov]
        polozky.append(
            {
                "nazov": nazov,
                "cena": cena,
                "kategoria": kategoria,
                "pocet": kosik.count(nazov),
                "na_sklade": kusy,
            }
        )
    return {
        "polozky": polozky,
        "zlava": stav["zlava"],
        "celkova_cena": spocitaj_cenu(),
    }


@app.get("/")
def index():
    return FileResponse(Path(__file__).parent / "index.html")


@app.get("/admin")
def admin():
    return FileResponse(Path(__file__).parent / "admin.html")


@app.get("/api/sklad")
def get_sklad():
    return [
        {"nazov": n, "cena": c, "kategoria": k, "kusy": q}
        for n, (c, k, q) in sklad.items()
    ]


@app.post("/api/sklad/{polozka}/pridaj")
def pridaj_kusy(polozka: str, data: PridanieKusov):
    polozka = polozka.lower().strip()
    if polozka not in sklad:
        raise HTTPException(status_code=404, detail="Taká položka v sklade nie je")

    cena, kategoria, kusy = sklad[polozka]
    nove_kusy = kusy + data.pocet
    sklad[polozka] = (cena, kategoria, nove_kusy)
    return {
        "sprava": f"Pridaných {data.pocet} ks: {polozka}. Na sklade je teraz {nove_kusy} ks.",
        "nazov": polozka,
        "kusy": nove_kusy,
    }


@app.get("/api/kosik")
def get_kosik():
    return vypis_kosika()


@app.post("/api/kosik/{polozka}")
def pridaj_do_kosika(polozka: str):
    polozka = polozka.lower().strip()
    if polozka not in sklad:
        raise HTTPException(status_code=404, detail="Taká položka v sklade nie je")

    cena, kategoria, kusy = sklad[polozka]
    if kusy <= 0:
        raise HTTPException(status_code=400, detail="Položka je vypredaná")

    kosik.append(polozka)
    sklad[polozka] = (cena, kategoria, max(kusy - 1, 0))
    return {
        "sprava": f"Pridané do košíka: {polozka} ({cena} €). Na sklade zostáva {kusy - 1} ks.",
        **vypis_kosika(),
    }


@app.post("/api/zlava")
def pouzi_kupon():
    if stav["zlava"]:
        raise HTTPException(status_code=400, detail="Kupón je už použitý")
    if not kosik:
        raise HTTPException(status_code=400, detail="Košík je prázdny")
    stav["zlava"] = True
    return {"sprava": "Super, 10 % zľava bola aplikovaná.", **vypis_kosika()}


@app.post("/api/reset")
def reset():
    global sklad
    sklad = copy.deepcopy(SKLAD_POVODNY)
    kosik.clear()
    stav["zlava"] = False
    return {"sprava": "Obchod bol resetovaný.", **vypis_kosika()}
