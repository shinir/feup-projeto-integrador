import requests
from bs4 import BeautifulSoup

# specify the url of the .asp webpage to scrape
url = "https://dges.gov.pt/coloc/2022/col1listaser.asp"

header_params = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15",
    "Accept-Language": "en-GB,en;q=0.9",
    "Referer": "https://dges.gov.pt/coloc/2022/col1listaredir.asp"
}

# Define any request data parameters
request_data = {
    "CodCurso": "L224",
    "CodR": "11",
    "CodEstab": "1105",
    "search": "Continuar"
}

# send a GET request to the webpage
response = requests.get(url, headers=header_params, params=request_data)

# create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

tables = soup.find_all('table', {'class': 'caixa'})

table = tables[0]

tbody = table.find('tbody')

rows = tbody.find_all('tr')

for row in rows:
    cells = row.find_all('td')
    for cell in cells:
        print(cell.text)


# print the scraped content to the console
# title = soup.title.string
# print(title)
