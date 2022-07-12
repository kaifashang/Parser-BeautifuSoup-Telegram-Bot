import requests
from bs4 import BeautifulSoup
import json
import re


def html_parser():
    data = []
    for p in range(1, 1000):
        print(p)
        url = (f'https://aliexpress.ru/category/202040673/smart-watches/'
               f'w-умные%20часы%20xiaomi?'
               f'spm=a2g2w.productlist.0.0.eb103c71SNp7IX&pvid='
               f'43-201454275&shipFromCountry='
               f'CN&isFreeShip=y&isFavorite=y&page={p}')
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')

        watchs = soup.findAll(
            'div', class_='product-snippet_ProductSnippet__content__tusfnx')

        n = int(re.findall(r'\d+', (soup.find(
            'div',
            class_='SearchPagination_SearchPagination__pagination__wjhu3'
            ).find(
            'span', class_='SearchPagination_SearchPagination__label__wjhu3'
            ).text.split()[1]))[0])

        if p == n:
            break

    try:
        for watch in watchs:
            discount = watch.find(
                'div', class_='snow-price_SnowPrice__discountPercent__2y0jkd'
                ).text
            link = "https://aliexpress.ru" + watch.find(
                'a',
                class_='product-snippet_ProductSnippet__galleryBlock__tusfnx'
                ).get('href')
            name = watch.find(
                'div', class_='product-snippet_ProductSnippet__name__tusfnx'
                ).text
            photo = "https:" + watch.find(
                'img', class_='gallery_Gallery__image__1ln22f').get('src')

            data.append([discount, link, name, photo])

    except AttributeError:
        pass

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    html_parser()


if __name__ == "__main__":
    main()
