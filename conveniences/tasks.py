import re
import time
from datetime import date

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

from .models import Product


def get_driver():  # git에서 다운받은 SELENIUM_LAYER.zip을 사용했다면, 아래 설정 중 아무것도 건드리지 않는다.
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1280x1696')
    chrome_options.add_argument('--user-data-dir=/tmp/user-data')
    chrome_options.add_argument('--hide-scrollbars')
    chrome_options.add_argument('--enable-logging')
    chrome_options.add_argument('--log-level=0')
    chrome_options.add_argument('--v=99')
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--data-path=/tmp/data-path')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--homedir=/tmp')
    chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
    driver = webdriver.Chrome('/Users/taxijjang/personal_git_dir/convenience_store_discount/webdriver/chromedriver',
                              chrome_options=chrome_options)
    return driver


def seven_eleven_store():
    """
    seven_eleven 상품
    """
    BASE_URL = "https://www.7-eleven.co.kr"
    seven_eleven_store_url = f"{BASE_URL}/product/presentList.asp"
    driver = get_driver()
    driver.get(seven_eleven_store_url)

    sale_products = {
        "1+1": 1,
        "2+1": 2,
        "sale_product": 3,
        "present_product": 4,
    }

    seven_eleven_products = list()
    # 모든 상품 스크롤
    for sale_type, value in sale_products.items():
        print(f"---------------------{sale_type} - {value} ----------------------- ")
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, f"#actFrm > div.cont_body > div.wrap_tab > ul > li:nth-child({value}) > a"))
        )
        time.sleep(2)
        element.send_keys(Keys.ENTER)
        time.sleep(2)
        try:
            while True:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#listUl > li.btn_more > a'))
                )
                time.sleep(2)
                element.send_keys(Keys.ENTER)
                time.sleep(2)
                print(1111)

        except Exception:
            print("모든 상품 페이지 스크롤 완료")

        for product in driver.find_elements(By.CSS_SELECTOR, '#listUl > li > div'):
            title, price = product.text.split('\n')
            price = re.sub(r'[^0-9]', '', price)
            image = f"{BASE_URL}{BeautifulSoup(product.get_attribute('innerHTML'), 'html.parser').find('img').get('src')}"
            print(sale_type, title, price, image)
            seven_eleven_products.append(
                Product.objects.get_or_create(
                    year=date.today().year,
                    month=date.today().month,
                    conveniences_store=Product.SEVEN_ELEVEN,
                    title=title,
                    price=price,
                    image=image,
                    sale_type=sale_type,
                ),
            )


def emart_store():
    """
    emart24 상품
    """
    BASE_URL = "https://emart24.co.kr/product/eventProduct.asp"
    driver = get_driver()
    driver.get(BASE_URL)

    seven_eleven_products = list()
    # 모든 상품 리스트

    while True:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#regForm > div.section > div.eventProduct > div.tabContArea > ul > li"))
        )
        elements = driver.find_elements(By.CSS_SELECTOR,
                                        "#regForm > div.section > div.eventProduct > div.tabContArea > ul > li> div")
        for element in elements:
            try:
                data = element.text.split('\n')
                title, price = data[-2:]
                price = re.sub(r'[^0-9→]', '', price)
                discount_price = price
                WebDriverWait(element, 10).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "div > p.productImg > img")
                    )
                )
                image = element.find_element(By.CSS_SELECTOR, "div > p.productImg > img").get_attribute("src")

                WebDriverWait(element, 10).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "div > div > p > img")
                    )
                )
                sale_type = re.sub(r'[^0-9+]', '',
                                   element.find_element(By.CSS_SELECTOR, "div > div > p > img").get_attribute("alt"))
                if not sale_type:
                    sale_type = Product.SALE_PRODUCT
                    price, discount_price = price.split('→')
                if sale_type == '2':
                    sale_type = Product.PRESENT_PRODUCT
                print(sale_type, title, price, image)
                Product.objects.get_or_create(
                    year=date.today().year,
                    month=date.today().month,
                    conveniences_store=Product.EMART,
                    title=title,
                    price=price,
                    discount_price=discount_price,
                    image=image,
                    sale_type=sale_type,
                )
            except Exception:
                print(sale_type, title, price, image)
                pass

        next_icon_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#regForm > div.section > div.eventProduct > div.paging > a.next.bgNone"))
        )

        next_element = driver.find_element(By.CSS_SELECTOR,
                                           "#regForm > div.section > div.eventProduct > div.paging > a.next.bgNone")
        if next_element.get_attribute("href") == f"{BASE_URL}#none":
            break
        next_icon_element.send_keys(Keys.ENTER)
        time.sleep(2)


def main():
    seven_eleven_store()
    emart_store()


if __name__ == '__main__':
    main()
