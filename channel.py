from bs4 import BeautifulSoup
import requests


start_url = 'http://bj.58.com/sale.shtml'
url_host = 'http://bj.58.com'

def get_index_url(url):
    # url = start_url
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select('ul.ym-submnu > li > b > a')
    for link in links:
        page_url = url_host + link.get('href')
        print(page_url)

get_index_url(start_url)

channel_list = '''
    http://bj.58.com/shouji/
'''