from multiprocessing import Pool
from channel_extact  import channel_list
from pages_parsing   import get_links_from, url_list,get_item_info





def get_all_links_from(channel):
    for i in range(1, 60):
        get_links_from(channel, i)



if __name__ == '__main__':
    pool = Pool()
    # pool = Pool(processes=6)
    pool.map(get_all_links_from, channel_list.split())
    db_urls = [item['url'] for item in url_list.find()]
    pool.map(get_item_info, db_urls)
    pool.close()
    pool.join()