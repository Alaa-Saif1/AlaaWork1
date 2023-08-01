import requests
from bs4 import BeautifulSoup
import json

def scrape_scientist_data(name):
    url = f"https://en.wikipedia.org/wiki/{name}"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    info_table = soup.select_one('.infobox')
    rows = info_table.select('tr')

    scientist_data = {}
    for row in rows:
        header = row.select_one('th')
        if header:
            header_text = header.get_text().strip()
            value = row.select_one('td')
            if value:
                value_text = value.get_text().strip()
                scientist_data[header_text] = value_text

    with open('scientist_data.json', 'w') as file:
        json.dump(scientist_data, file, indent=4)

    print(f"Scientist: {name}")
    for key, value in scientist_data.items():
        print(f"{key}: {value}")

name = input("Enter a scientist's name: ")

scrape_scientist_data(name)