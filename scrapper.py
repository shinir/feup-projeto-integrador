import os
import click
import requests
import csv
from bs4 import BeautifulSoup

def scrap(codCurso, codR, codEstab, ano, types, filepath):
    # Request Data that passes through the web
    request_data = {
        "CodCurso": codCurso,
        "CodR": codR,
        "CodEstab": codEstab,
        "search": "Continuar"
    }

    #Candidatos
    if types == "0":
        print("Candidatos")
        url = "https://dges.gov.pt/coloc/" + ano + "/col1listaser.asp?CodEstab=" + codEstab + "&CodCurso=" + codCurso + "&ids=1&ide=2000&Mx=2000"

    # Colocados
    elif types == "1":
        print("Colocados")
        url = "https://dges.gov.pt/coloc/" + ano + "/col1listacol.asp"

    else:
        raise Exception("O tipo de dados selecionado encontra-se indisponível.")
    
    response = requests.get(url, data=request_data)
    soup = BeautifulSoup(response.content, "html.parser")

    tables = soup.find_all('table', {'class': 'caixa'})
    table = tables[2]
    rows = table.find_all('tr')

    with open(filepath, "w", newline="") as csvfile:
        writer = csv.writer(csvfile,delimiter=';')
        writer.writerow(["id", "codigo", "nome", "media", "opcao", "pi", "ano12", "ano1011"])
        for row in table.find_all('tr'):
            cells = row.find_all('td')
            data = [col.get_text(strip=True).replace(',', '.') for col in cells]
            writer.writerow(data)
            #print(data)
            