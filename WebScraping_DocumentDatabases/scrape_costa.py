from bs4 import BeautifulSoup as bs
import requests

def scrape_info():

    url = 'https://visitcostarica.herokuapp.com/index.html'

    response = requests.get(url)

    soup = bs(response.text,'html.parser')

    for val in soup.find_all('div',id='weather'):
        temp_dict = {
            'max':val.find_all('strong')[1].text,
            'min':val.find_all('strong')[0].text
        }

    return temp_dict
    