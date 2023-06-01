import sqlite3
import requests
from bs4 import BeautifulSoup

# Connect to SQLite database
conn = sqlite3.connect('db/database.db')
c = conn.cursor()

# Scrape data from website

# Fetch curso data from the Curso table
c.execute('SELECT id, codigo, nome, ano, instituicao FROM Curso')
curso_data = c.fetchall()   

# Iterate over each curso and scrape data
for curso in curso_data:
    curso_id, codigo, nome, ano, instituicao = curso

    print(codigo + nome)

    request_data = {
        "CodCurso": codigo,
        "CodR": "11",
        "CodEstab": instituicao,
        "search": "Continuar"
    }

    # Replace with the URL of the website you want to scrape
    url_cand = "https://dges.gov.pt/coloc/" + str(ano) + "/col1listaser.asp?CodEstab=" + str(instituicao) + "&CodCurso=" + str(codigo) + "&ids=1&ide=3000&Mx=3000"
    url_col  = "https://dges.gov.pt/coloc/" + str(ano) + "/col1listacol.asp"
    
    response = requests.get(url_cand, data=request_data)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    try:

        # Scrape data for Candidatura table
        tables = soup.find_all('table', {'class': 'caixa'})
        table = tables[2]
        rows = table.find_all('tr')

        for row in table.find_all('tr'):
            cells = row.find_all('td')
            
            data = [col.get_text(strip=True).replace(',', '.') for col in cells]

            ids = int(data[0])
            codigo = data[1]
            nome = data[2]
            media = data[3]
            opcao = int(data[4])
            pi = float(data[5])
            ano12 = float(data[6])
            ano1011 = float(data[7])

            try:
                c.execute('INSERT INTO candidatura (id, codigo, nome, media, opcao, pi, ano12, ano1011, curso) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                    (ids, codigo, nome, media, opcao, pi, ano12, ano1011, curso_id))
            except sqlite3.IntegrityError:
                    # Handle constraint violation (e.g., print a message, log the error, etc.)
                    print(f"Skipping INSERT due to constraint violation: {row}")
            
        response = requests.get(url_col, data=request_data)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Scrape data for Colocado table
        tables = soup.find_all('table', {'class': 'caixa'})
        table = tables[2]
        rows = table.find_all('tr')

        for row in table.find_all('tr'):
            cells = row.find_all('td')
            
            data = [col.get_text(strip=True).replace(',', '.') for col in cells]

            codigo = data[0]
            nome = data[1]

            try:
                c.execute('INSERT INTO colocado (codigo, nome, curso) VALUES (?, ?, ?)',
                    (codigo, nome, curso_id))
            except sqlite3.IntegrityError:
                # Handle constraint violation (e.g., print a message, log the error, etc.)
                print(f"Skipping INSERT due to constraint violation: {row}")

    except IndexError:
         print(f"Index error, list index out of range: {row}")
# Commit changes and close connection
conn.commit()
conn.close()
