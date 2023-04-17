import os
import click
import requests
import csv
from bs4 import BeautifulSoup

@click.group()
def cli():
    pass
    #click.echo('Enter the type of document you intend to scrap:\n0 for candidates\n1 for the placed candidates\n')
    #click.echo("The course name inserted must be one of the following:\nLEIC, ISEP")

@click.option('--filename', prompt='Enter the output file name', help='Name of the output file')
@click.option('--course', prompt='Enter the course name\nLEIC, ISEP:')
@cli.command()
def candidatos(filename,course):
    if course.__eq__("LEIC"):
        url = "https://dges.gov.pt/coloc/2022/col1listaser.asp?CodEstab=1105&CodCurso=L224&ids=1&ide=2000&Mx=2000"
        request_data = {
            "CodCurso": "L224",
            "CodR": "11",
            "CodEstab": "1105",
            "search": "Continuar"
        }

    elif course.__eq__("ISEP"):
        url = "https://dges.gov.pt/coloc/2022/col1listaser.asp?CodEstab=3135&CodCurso=9119&ids=1&ide=2000&Mx=2000"
        request_data = {
            "CodCurso": "9119",
            "CodR": "12",
            "CodEstab": "3135",
            "search": "Continuar"
        }

    else:
        raise Exception("Course provided can't be processed")
    
    response = requests.get(url, data=request_data)
    soup = BeautifulSoup(response.content, "html.parser")

    tables = soup.find_all('table', {'class': 'caixa'})
    table = tables[2]
    rows = table.find_all('tr')

    filepath = os.path.join("csv/", filename)
    with open(filepath + ".csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile,delimiter=';')
        #writer.writerow(["identifier", "codigo", "nome", "media", "opcao", "pi", "ano12", "ano1011"])
        for row in table.find_all('tr'):
            cells = row.find_all('td')
            data = [col.get_text(strip=True).replace(',', '.') for col in cells]
            writer.writerow(data)

    print('Web scraping complete. Data saved to ' + filename + '.csv.')


@click.option('--filename', prompt='Enter the output file name', help='Name of the output file')
@cli.command()
def colocados(filename):
    # specify the url of the .asp webpage to scrape
    url = "https://dges.gov.pt/coloc/2022/col1listacol.asp"

    # Define any request data parameters
    request_data = {
        "CodCurso": "L224",
        "CodR": "11",
        "CodEstab": "1105",
        "search": "Continuar"
    }

    response = requests.get(url, data=request_data)
    soup = BeautifulSoup(response.content, "html.parser")

    tables = soup.find_all('table', {'class': 'caixa'})
    table = tables[2]
    rows = table.find_all('tr')

    filepath = os.path.join("csv/", filename)

    with open(filepath + ".csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile,delimiter=';')
        for row in table.find_all('tr'):
            cells = row.find_all('td')
            data = [col.get_text(strip=True) for col in cells]
            # Write the data to a row in the CSV file
            writer.writerow(data)
    
    print('Web scraping complete. Data saved to ' + filename + '.csv.')

@click.command()
def exit_program():
    print('Exiting program...')
    raise SystemExit

cli.add_command(candidatos)
cli.add_command(colocados)
cli.add_command(exit_program)

if __name__ == '__main__':
    cli()