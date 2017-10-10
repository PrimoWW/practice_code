"""
from page 65
"""
import csv
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Comparison_of_text_editors"

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
# we only need the first table
table = soup.findAll("table", {"class": "wikitable"})[0]
rows = table.findAll("tr")

csvFile = open("editors.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()