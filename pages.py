from bs4 import BeautifulSoup
import requests
import time
import random
import pymongo

client = pymongo.MongoClient('localhost', 27017)
ceshi = client['58tongcheng']
url_list = ceshi['url_list4']
item_info = ceshi['item_info4']


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Connection':'keep-alive'
}

proxy_list = [
    'http://125.88.74.122:83',
    'http://183.61.236.54:3128',
    'http://61.166.151.82:8080',
    ]
proxy_ip = random.choice(proxy_list)
proxies = {'http': proxy_ip}


#http://bj.58.com/shouji/1/pn2/

def get_links_from(channel, pages, who_sells=1):
    # td.t 没有这个就终止
    list_view = '{}{}/pn{}/'.format(channel, str(who_sells), str(pages))
    wb_data = requests.get(list_view, headers=headers, proxies=proxies)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if soup.find('td', 't'):
        for link in soup.select('td.t a.t'):
            item_link = link.get('href').split('?')[0]
            url_list.insert_one({'url': item_link})
            print(item_link)
            # return urls
    else:
        # It's the last page !
        pass


def get_item_info(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    title = soup.title.text.strip()
    price = soup.select('span.price.c_f50')[0].text.strip() if len(soup.select('span.price.c_f50')) else None
    date = soup.select('.time')[0].text.strip() if len(soup.select('.time')) else None
    item_info.insert_one({'title': title, 'price': price, 'date': date, 'url': url})
    print({'title': title, 'price': price, 'date': date, 'url': url})



