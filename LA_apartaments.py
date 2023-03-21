from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests

main_link = 'https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'

google_form = 'https://docs.google.com/forms/d/e/1FAIpQLSeku5l8br0XJGFsoBIZj6UEaZQTuuziCMqKV03_h7QJQ8BPPQ/viewform?usp=sf_link'


class ApartmentFinder:
    def __init__(self):
        self.link = main_link
        self.form = google_form
        self.links_to_apartments = []
        self.prices = []
        self.addresses = []

    def get_data(self):

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0",
                   "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7"}

        response = requests.get('https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D', headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')

        apartments = soup.find_all(
            'img', {"aria-hidden": "false", "draggable": "auto"})
        price_spans = soup.find_all(
            'span', {'data-test': 'property-card-price'})

        for apartment in apartments:
            addresses = apartment["alt"]
            links = apartment["src"]
            self.addresses.append(addresses)
            self.links_to_apartments.append(links)

        for span in price_spans:
            price = span.text.strip()
            price = price.replace(',', '').replace(
                '+', '').replace('$', '').replace('/mo', '').replace(' 1 bd', '').strip()
            self.prices.append(price)

    def submit_data(self):
        
        driver = webdriver.Edge(
            executable_path=r"C:\Program Files\Development\MicrosoftWebDriver.exe")
        driver.get(self.form)

        for apartment in range(len(self.addresses)):
            question_1 = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            question_1.send_keys(self.addresses[apartment])

            question_2 = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            question_2.send_keys(self.links_to_apartments[apartment])

            question_3 = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            question_3.send_keys(self.prices[apartment])

            confirm = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            confirm.click()

            another_questions = driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            another_questions.click()
            
        driver.quit()



if __name__ == '__main__':
    finder = ApartmentFinder()
    finder.get_data()
    finder.submit_data()
