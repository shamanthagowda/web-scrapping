from bs4 import BeautifulSoup
import requests
import html5lib
import pandas as pd


def link_gen(product_name, last_page):
    product_name = product_name.replace(' ', '+')
    for page in range(1, last_page + 1):
        url = f'https://www.amazon.com/s?k={product_name}&page={page}&ref=nb_sb_noss_{page}'
        pages_urls.append(url)


#         linka sre generated and stored in the list


pages_urls = []
product_details = []

product_name = str(input('enter the product name  '))
total_pages = int(input('enter the number of pages  '))
# user input of product name and pages

# calling the link generating functio link_gen
link_gen(product_name, total_pages)
pages_urls

for url in pages_urls:

    #     requesting html page for each link
    html_file = requests.get(url)

    #     creating soupe object
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    #     itterating over each objects
    for individual in main:
        name = individual.find('h2', class_='a-size-mini a-spacing-none a-color-base s-line-clamp-2').text.strip()

        #        cheking wether the price is present of not
        if individual.find('span', class_='a-offscreen') == None:
            price = np.nan
        else:
            price = individual.find('span', class_='a-offscreen').text

        ratings = individual.find('span', class_='a-icon-alt').text
        ratings = ratings[0:3]

        reviews = individual.find('span', class_='a-size-base').text.strip()

        prod_link = individual.find('a', class_='a-link-normal a-text-normal')['href']
        prod_link = 'https://www.amazon.com' + str(prod_link)

        #       ading to the empty list
        product_details.append((name, price, ratings, reviews, prod_link))

df = pd.DataFrame(product_details, columns=['Product_Name', 'Price', 'Ratings', 'Reviews', 'Link_to_buy'])
df.to_csv('C:\\Users\\shama\\Desktop\\python\\web scrapping\\files\\amazon_ultrawide_monitors.csv', index=False)