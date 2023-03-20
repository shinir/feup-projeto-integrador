import click
import requests
import csv
from bs4 import BeautifulSoup

@click.group()
def cli():
    pass

@click.option('--filename', prompt='Enter the output file name', help='Name of the output file')
@cli.command()
def candidatos(filename):

    # specify the url of the .asp webpage to scrape
    url = "https://dges.gov.pt/coloc/2022/col1listaser.asp?CodEstab=1105&CodCurso=L224&ids=1&ide=1140&Mx=1140"

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

    with open(filename + ".csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Id", "Name"])
        for row in table.find_all('tr'):
            cells = row.find_all('td')
            data = [col.get_text(strip=True) for col in cells]
            # Write the data to a row in the CSV file
            writer.writerow(data)
    
    print('Web scraping complete. Data saved to data.csv.')


@click.option('--filename', prompt='Enter the output file name', help='Name of the output file')
@cli.command()
def colocados(filename):

    import requests
    import csv
    from bs4 import BeautifulSoup

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

    with open(filename + ".csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Id", "Name"])
        for row in table.find_all('tr'):
            cells = row.find_all('td')
            data = [col.get_text(strip=True) for col in cells]
            # Write the data to a row in the CSV file
            writer.writerow(data)
    
    print('Web scraping complete. Data saved to data.csv.')

@click.command()
def exit_program():
    print('Exiting program...')
    raise SystemExit

cli.add_command(candidatos)
cli.add_command(colocados)
cli.add_command(exit_program)

if __name__ == '__main__':
    cli()