import pandas as pd
import numpy as np
import html5lib
from bs4 import BeautifulSoup
from msedge.selenium_tools import Edge, EdgeOptions
import requests


def url_gen(product_name, total_pages):
    product_name = product_name.replace(' ', '+')
    for page in np.arange(1, total_pages + 1):
        url = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw={product_name}&_sacat=0&LH_TitleDesc=0&rt=nc&_pgn={page}'
        urls.append(url)


options = EdgeOptions()
options.use_chromium = True
driver = Edge('C:\\Users\\shama\\Downloads\\edgedriver_win32\\msedgedriver.exe', options=options)

urls = []
product_name = str(input('enter product name  '))
total_pages = int(input('enter number of pages  '))

url_gen(product_name, total_pages)

prod_list = []

for url_itter in urls:
    driver.get(url_itter)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    main = soup.find_all('div', class_='s-item__wrapper clearfix')
    main = main[1:]
    for ind in main:
        name = ind.find('h3', class_='s-item__title').text

        price = ind.find('span', class_='s-item__price').text
        price_req = price.replace('$', '')
        #         price_req=float(price_req)

        shipping_cost = ind.find('span', class_='s-item__shipping s-item__logisticsCost').text
        #         shipping_cost=main[1].find('span',class_='s-item__shipping s-item__logisticsCost').text
        #         shipping_cost_req=shipping_cost_req.replace('+$','')
        #         shipping_cost_req=shipping_cost_req.replace(' shipping','')
        #         shipping_cost_req=shipping_cost_req[:-3]

        #         if shipping_cost_req=='Free International Shipping':
        #             shipping_cost_req=0
        #         elif shipping_cost_req=='Shipping not specified':
        #             shipping_cost_req=np.nan
        #         else:
        #             shipping_cost_req=float(shipping_cost_req)

        from_country = ind.find('span', class_='s-item__location s-item__itemLocation').text

        secondary_info = ind.find('span', class_='SECONDARY_INFO').text

        link = ind.find('a', class_='s-item__link')['href']
        #         total_price=shipping_cost_req+price_req
        #         total_price='$ '+str(total_price)
        prod_list.append((name, price, shipping_cost, from_country, secondary_info, link))

df = pd.DataFrame(prod_list, columns=['Product Name', 'Price', 'Shipping Cost', 'Country', 'Secondary Info', 'Link'])
df = df.drop_duplicates(subset='Product Name', keep='first')
df
df.to_csv('C:\\Users\\shama\\Desktop\\python\\web scrapping\\files\\ebay_data_mobiles.csv', index=False)