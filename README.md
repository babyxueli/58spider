关于本次爬取的相关介绍和心得：
    1.本次爬取的目的主要是为了获取58同城某一手机网页关于二手手机的相关数据，
    首先要获取想要进行爬取数据的某一分支，这里指的就是手机栏目，其次在其分支下
    获取相关的手机的价格、日期等信息。选取58上的前六十页并保存在使用的数据库中。
    
    2使用的程序有四部分，channel.py主要用来获取我想要爬取的手机信息主要分支，pages.py用来获取手机下面
的前六十页的相关信息并分类保存在数据库中，counts.py主要用来记录我要爬取数据的总数，main.py用来运行主
要的爬虫程序。
 
    3将爬取的数据从数据库导出，并以excel格式保存。
