from bs4 import BeautifulSoup as bs
import requests

def scrape_info():

    url = 'https://visitcostarica.herokuapp.com/index.html'

    response = requests.get(url)

    soup = bs(response.text,'html.parser')

    # Link for Image (still needs work)
    for link in soup.find_all('img',class_='img-fluid animals'):
        img = link['src']
        break
    # Image
    
    for val in soup.find_all('div',id='weather'):
        temp_dict = {
            'max':val.find_all('strong')[1].text,
            'min':val.find_all('strong')[0].text
        }


    url = 'https://houston.craigslist.org/search/pet?s=100'
    response = requests.get(url)

    soup = bs(response.text,'html.parser')
    craig_dict = []
    for val in soup.find_all('p',class_='result-info'):
        craig = {'title':val.a.text,'link':val.a['href']}
        craig_dict.append(craig)

    return temp_dict, craig_dict
    