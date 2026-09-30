from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

# Sklad a stav aplikácie (podľa tvojho kódu)
sklad = {
    "jablko": {"cena": 1.0, "kategoria": "ovocie", "kusy": 2},
    "ananas": {"cena": 1.3, "kategoria": "ovocie", "kusy": 500},
    "mrkva": {"cena": 0.2, "kategoria": "zelenina", "kusy": 800},
    "kitkat": {"cena": 0.8, "kategoria": "sladkosti", "kusy": 300},
    "kinder": {"cena": 1.5, "kategoria": "sladkosti", "kusy": 100}
}

kosik = []
zlava_aplikovana = False
sprava = ""

def vypocitaj_celkovu_cenu():
    suma = sum(item["cena"] for item in kosik)
    if zlava_aplikovana:
        suma = round(suma * 0.9, 2)
    return round(suma, 2)

def generuj_html():
    global sprava
    
    # Riadky skladu
    sklad_html = ""
    for nazov, detail in sklad.items():
        tlacidlo = (
            f'<form action="/pridat" method="post" style="margin:0;">'
            f'<input type="hidden" name="polozka" value="{nazov}">'
            f'<button type="submit" style="background:#28a745;color:white;border:none;padding:5px 10px;border-radius:3px;cursor:pointer;">Pridať do košíka</button>'
            f'</form>'
        ) if detail["kusy"] > 0 else '<span style="color:red;font-weight:bold;">Vypredané</span>'
        
        sklad_html += f"""
        <tr>
            <td><b>{nazov.capitalize()}</b></td>
            <td>{detail['cena']:.2f} €</td>
            <td>{detail['kategoria']}</td>
            <td>{detail['kusy']} ks</td>
            <td>{tlacidlo}</td>
        </tr>
        """

    # Položky v košíku
    kosik_html = ""
    if kosik:
        kosik_html += "<ul>"
        for item in kosik:
            kosik_html += f"<li>{item['nazov'].capitalize()} – {item['cena']:.2f} € (<i>{item['kategoria']}</i>)</li>"
        kosik_html += "</ul>"
    else:
        kosik_html = "<p>Váš košík je prázdny.</p>"

    celkova_cena = vypocitaj_celkovu_cenu()
    
    # Formulár na zľavu
    zlava_html = ""
    if kosik and not zlava_aplikovana:
        zlava_html = """
        <form action="/zlava" method="post" style="margin-top:15px;">
            <label><b>Máte zľavový kupón?</b> (skús 10% kupon):</label><br>
            <input type="text" name="kupon" placeholder="Zadaj 'ano' alebo '10%'" style="padding:5px;margin-top:5px;">
            <button type="submit" style="padding:5px 10px;">Uplatniť</button>
        </form>
        """
    elif zlava_aplikovana:
        zlava_html = "<p style='color:green;'><b>10% zľava bola uplatnená!</b></p>"

    html = f"""
    <!DOCTYPE html>
    <html lang="sk">
    <head>
        <meta charset="UTF-8">
        <title>Nákupný Košík</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 30px; background-color: #f4f4f9; }}
            h1 {{ color: #333; }}
            .container {{ display: flex; gap: 30px; }}
            .box {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); flex: 1; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #007bff; color: white; }}
            .sprava {{ padding: 10px; background: #e2e3e5; margin-bottom: 20px; border-radius: 4px; border-left: 5px solid #007bff; }}
        </style>
    </head>
    <body>
        <h1>🛒 Vitajte v obchode</h1>
        
        {f'<div class="sprava">{sprava}</div>' if sprava else ''}

        <div class="container">
            <!-- SKLAD -->
            <div class="box">
                <h2>Sklad</h2>
                <table>
                    <tr>
                        <th>Položka</th>
                        <th>Cena</th>
                        <th>Kategória</th>
                        <th>Skladom</th>
                        <th>Akcia</th>
                    </tr>
                    {sklad_html}
                </table>
            </div>

            <!-- KOŠÍK -->
            <div class="box">
                <h2>Váš Košík</h2>
                {kosik_html}
                <hr>
                <p style="font-size: 1.2em;"><b>Celková cena:</b> {celkova_cena:.2f} €</p>
                {zlava_html}
                
                {'''
                <form action="/reset" method="post" style="margin-top:20px;">
                    <button type="submit" style="background:#dc3545;color:white;border:none;padding:8px 12px;border-radius:3px;cursor:pointer;">Resetovať nákup</button>
                </form>
                ''' if kosik else ''}
            </div>
        </div>
    </body>
    </html>
    """
    return html

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(generuj_html().encode('utf-8'))

    def do_POST(self):
        global zlava_aplikovana, sprava
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = urllib.parse.parse_qs(post_data)

        if self.path == '/pridat':
            polozka = params.get('polozka', [''])[0]
            if polozka in sklad:
                if sklad[polozka]['kusy'] > 0:
                    sklad[polozka]['kusy'] -= 1
                    kosik.append({
                        "nazov": polozka,
                        "cena": sklad[polozka]["cena"],
                        "kategoria": sklad[polozka]["kategoria"]
                    })
                    sprava = f"Pridané do košíka: <b>{polozka}</b> ({sklad[polozka]['cena']} €)"
                else:
                    sprava = f"Položka <b>{polozka}</b> je vypredaná!"

        elif self.path == '/zlava':
            kupon = params.get('kupon', [''])[0].strip().lower()
            if kupon in ['ano', '10%', '10', 'ano ']:
                zlava_aplikovana = True
                sprava = "Super! 10% zľava bola uplatnená."
            else:
                sprava = "Neplatný zľavový kupón."

        elif self.path == '/reset':
            # Vrátenie tovaru na sklad pri resete
            for item in kosik:
                sklad[item['nazov']]['kusy'] += 1
            kosik.clear()
            zlava_aplikovana = False
            sprava = "Košík bol resetovaný a tovar vrátený na sklad."

        # Presmerovanie späť na hlavnú stránku (PRG pattern)
        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server beží na adrese http://localhost:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
