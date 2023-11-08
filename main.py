import re
import sys
import requests
from bs4 import BeautifulSoup

REGULAR = '[+]?[7|8]?[(]?[0-9]{3}[)]?[0-9]{3}[-]?[0-9]{2}[-]?[0-9]{2}'

def parse(url):
    page = requests.get(url).content
    soup = BeautifulSoup(page, 'html.parser')
    with open(f'{''.join(url.split(r'//')[1:])}.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    text = soup.get_text().replace(' ', '')
    list_of_numbers = re.findall(REGULAR, text)
    list_of_numbers = list(set(list_of_numbers))
    answer = []
    for mobile in list_of_numbers:
        mobile = mobile.replace('+7', '8')
        mobile = mobile.replace('-', '')
        mobile = mobile.replace('(', '')
        mobile = mobile.replace(')', '')
        answer.append(mobile)
    return answer

if __name__ == "__main__":
    if len(sys.argv) > 1:
        phones = parse(sys.argv[1])
        for phone in phones:
            print(phone)
    else:
        print("Error: no url for parse")

