import requests
from bs4 import BeautifulSoup
import re

from .models import Car


class Scraper:
    def __init__(self, brand, name, model, kilometer, accuracy):
        self.accuracy = accuracy
        self.brand = brand
        self.name = name
        self.model = model
        min_kilometer = int(kilometer) - 50000 if int(kilometer) > 51000 else kilometer

        page = f"https://divar.ir/s/iran/car/{brand}?production-year={model}-{model}&usage={min_kilometer}-{int(kilometer) + 50000}&q={name}"
        request = requests.get(page)
        page_soup = BeautifulSoup(request.text, 'html.parser')
        cars = page_soup.find_all('div', attrs={'class': 'post-card-item kt-col-6 kt-col-xxl-4'})
        count = 0
        while count < accuracy:
            for car in cars:
                check = re.search(r'تومان', str(car.text))
                if check:
                    car_link = re.findall(r'href=\"(.*?)\"', str(car))
                    url = f'https://divar.ir{car_link[0]}'

                    r = requests.get(url)
                    soup = BeautifulSoup(r.text, 'html.parser')
                    check_name = soup.find_all('a', attrs={'class': 'kt-unexpandable-row__action kt-text-truncate'})
                    if len(check_name) == 2:
                        self.name = check_name[1].text
                    elif len(check_name) == 1:
                        self.name = check_name[0].text
                    kyc = soup.find_all("span", attrs={"class": "kt-group-row-item__value"})
                    # self.kilometer = kyc[0].text
                    # self.model = kyc[1].text
                    # self.color = kyc[2].text
                    # self.price = re.findall(r'>(\d+٬\d+٬\d.+) تومان.*?</p></div></div><hr', str(soup))[0]

                    Car.objects.create(name=self.name, price=re.findall(r'>(\d+٬\d+٬\d.+) تومان.*?</p></div></div><hr', str(soup))[0], kilometer=kyc[0].text, model=kyc[1].text)
                    count += 1
                    if count == accuracy:
                        break
