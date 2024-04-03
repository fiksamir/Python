# Збір даних відеокарт з сайту rozetka.ua

################
import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

header = {
    'User-Agent':
         'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/117.0',
    'Accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}


def get_data_by_selenium(url: str) -> str:
    """ Звертається до сервера за url адресою і повертає HTML сайту"""
    service = Service(path="geckodriver")
    driver = webdriver.Firefox(service=service)
    driver.get(url)
    time.sleep(3)
    data = driver.page_source
    driver.quit()
    return data


def parse_data(data: str) -> list:
    """ Функція парсингу даних з хтмл документа"""
    rez = []
    if data:
        soup = BeautifulSoup(data, 'html.parser')
        li_list = soup.find_all('li', attrs={'class': 'catalog-grid__cell'})
        for li in li_list:
            # Пошук тега а
            a = li.find('a', attrs={'class': 'goods-tile__heading'})
            # Беремо у тега а атрибут href
            href = a['href']
            # За допомогою атрибуту текст, забираємо всю текстову
            # інформацію, що міститься в цьому тегу
            title = a.text
            old = li.find('div', attrs={'class': 'goods-tile__price--old'})
            price = li.find('div', attrs={'class': 'goods-tile__price'})
            # Стара ціна є не у всіх, тому потрібно зробити дефолтне значення
            old_price = ''
            if old:
                # Якщо контейнер із старою ціною є
                old = old.text
                # І в цьому контейнер є інфа
                if old:
                    # Забираємо лише те, що є цифрами та формуємо значення ціни
                    old_price = int(''.join(c for c in old if c.isdigit()))  #14500
            # Звичайна ціна є скрізь, тому формуємо значення
            price = int(''.join(c for c in price.text if c.isdigit()))
            # Результат за кожною відеокартою записуємо у вигляді словника
            rez.append({
                'title': title, 'href': href, 'price': price,
                'old_price': old_price
            })
    return rez


def save_to_csv(rows) -> None:
    """Функція збереження даних у csv-файл"""
    csv_title = ['title', 'href', 'price', 'old_price', ]
    with open('videocards.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    """ Головна функція диригент"""
    url = 'https://hard.rozetka.com.ua/videocards/c80087/page={}/'
    rows = []
    for i in range(1, 3):
        data = get_data_by_selenium(url.format(i))
        rows += parse_data(data)
        time.sleep(3)

    save_to_csv(rows)


if __name__ == '__main__':
    main()