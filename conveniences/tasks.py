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

from conveniences.models.product import Product


def get_driver():  # git에서 다운받은 SELENIUM_LAYER.zip을 사용했다면, 아래 설정 중 아무것도 건드리지 않는다.
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--window-size=1280x1696')
    # chrome_options.add_argument('--user-data-dir=/tmp/user-data')
    # chrome_options.add_argument('--hide-scrollbars')
    # chrome_options.add_argument('--enable-logging')
    # chrome_options.add_argument('--log-level=0')
    # chrome_options.add_argument('--v=99')
    # chrome_options.add_argument('--single-process')
    # chrome_options.add_argument('--data-path=/tmp/data-path')
    # chrome_options.add_argument('--ignore-certificate-errors')
    # chrome_options.add_argument('--homedir=/tmp')
    # chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    # driver = webdriver.Chrome('/Users/taxijjang/personal-git-dir/django_shopping_mall_api_project/conveniences/webdriver/chromedriver', chrome_options=chrome_options)
    return driver


def seven_eleven_store():
    """
    seven_eleven 상품
    """
    BASE_URL = "https://www.7-eleven.co.kr/product/presentList.asp"
    IMAGE_BASE_URL = "https://www.7-eleven.co.kr"
    driver = get_driver()
    driver.get(BASE_URL)
    driver.implicitly_wait(10)

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, f"#actFrm > div.cont_body > div.wrap_tab > ul > li > a"))
    )
    product_category_elements = driver.find_elements(By.CSS_SELECTOR,
                                                     f"#actFrm > div.cont_body > div.wrap_tab > ul > li > a")
    # 모든 상품 스크롤
    # for product_category_element in product_category_elements:
    product_category_element = product_category_elements[1]
    sale_type = product_category_element.accessible_name
    driver.implicitly_wait(10)
    product_category_element.send_keys(Keys.ENTER)
    driver.implicitly_wait(10)
    time.sleep(1)
    try:
        while True:
            more_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#listUl > li.btn_more > a'))
            )
            driver.implicitly_wait(10)
            more_element.send_keys(Keys.ENTER)
            driver.implicitly_wait(10)
            time.sleep(3)

    except Exception:
        print("모든 상품 페이지 스크롤 완료")
    for product in driver.find_elements(By.CSS_SELECTOR, '#listUl > li > div'):
        title, price = product.text.split('\n')
        price = re.sub(r'[^0-9]', '', price)
        image = f"{IMAGE_BASE_URL}{BeautifulSoup(product.get_attribute('innerHTML'), 'html.parser').find('img').get('src')}"
        p, _ = Product.objects.get_or_create(
            year=date.today().year,
            month=date.today().month,
            store=Product.SEVEN_ELEVEN,
            title=title,
            price=price,
            image=image.replace("https", "http"),
            sale_type=sale_type,
        )

    driver.close()


def emart_store():
    """
    emart24 상품
    """
    BASE_URL = "https://emart24.co.kr/product/eventProduct.asp"
    driver = get_driver()
    driver.get(BASE_URL)
    driver.implicitly_wait(10)

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
                Product.objects.get_or_create(
                    year=date.today().year,
                    month=date.today().month,
                    store=Product.EMART,
                    title=title,
                    price=price,
                    discount_price=discount_price,
                    image=image.replace("https", "http"),
                    sale_type=sale_type,
                )
            except Exception:
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
    driver.close()


def cu_store():
    BASE_URL = "https://cu.bgfretail.com/event/plus.do?category=event&depth2=1&sf=N"
    driver = get_driver()
    driver.get(BASE_URL)
    driver.implicitly_wait(10)
    while True:
        try:
            next_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#contents > div.relCon > div > div > div.prodListBtn-w > a")))
            driver.implicitly_wait(10)
            next_element.send_keys(Keys.ENTER)
            driver.implicitly_wait(10)
            time.sleep(1)
        except Exception:
            break

    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "#contents > div.relCon > div > ul > li"))
    )
    for element in elements:
        title, price, _, sale_type = element.text.split('\n')
        image = element.find_element(By.CSS_SELECTOR, "a > div.prod_wrap > div.prod_img > img").get_attribute("src")
        Product.objects.get_or_create(
            year=date.today().year,
            month=date.today().month,
            title=title,
            price=re.sub(r'[^0-9]', '', price),
            store=Product.CU,
            image=image.replace("https", "http"),
            sale_type=sale_type,
        )
    driver.close()


def gs25_store():
    BASE_URL = "http://gs25.gsretail.com/gscvs/ko/products/event-goods#;"
    driver = get_driver()
    driver.get(BASE_URL)
    driver.implicitly_wait(10)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#contents > div.cnt > div.cnt_section.mt50 > div > div > ul > li:nth-child(4) > span > a")
        # (By.XPATH, "#contents > div.cnt > div.cnt_section.mt50 > div > div > ul > li:nth-child(4) > a")
    ))
    all_product_element = driver.find_element(By.CSS_SELECTOR,
                                              "#contents > div.cnt > div.cnt_section.mt50 > div > div > ul > li:nth-child(4) > span > a")
    driver.implicitly_wait(10)
    all_product_element.send_keys(Keys.ENTER)
    driver.implicitly_wait(10)
    time.sleep(1)

    sale_type_dict = {
        Product.ONE_PLUS_ONE: Product.ONE_PLUS_ONE,
        "덤증정": Product.PRESENT_PRODUCT,
    }
    while True:
        try:
            # 상품 크롤링
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "#contents > div.cnt > div.cnt_section.mt50 > div > div > div:nth-child(3) > ul > li")
            ))
            driver.implicitly_wait(10)
            product_elements = driver.find_elements(By.CSS_SELECTOR,
                                                    "#contents > div.cnt > div.cnt_section.mt50 > div > div > div:nth-child(3) > ul > li")
            driver.implicitly_wait(10)
            time.sleep(1)
            for product_element in product_elements:
                try:
                    img = str(product_element.find_element(By.CSS_SELECTOR, "div > p.img > img").get_attribute("src")).replace("https", "http")
                except Exception as e:
                    img = ""

                product_sale_type = product_element.find_element(By.CSS_SELECTOR, "div > div > p > span").get_attribute(
                    "innerHTML")
                Product.objects.get_or_create(
                    year=date.today().year,
                    month=date.today().month,
                    title=product_element.find_element(By.CSS_SELECTOR, "div > p.tit").get_attribute('innerHTML'),
                    price=re.sub(r'[^0-9]', '',
                                 product_element.find_element(By.CSS_SELECTOR, "div > p.price > span").get_attribute(
                                     "innerHTML")),
                    store=Product.GS25,
                    image=img,
                    sale_type=Product.PRESENT_PRODUCT if product_sale_type == "덤증정" else product_sale_type
                )
            # 다음 페이지로 이동
            driver.implicitly_wait(10)
            next_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 "#contents > div.cnt > div.cnt_section.mt50 > div > div > div:nth-child(9) > div > a.next")
            ))

            driver.implicitly_wait(10)
            next_element.send_keys(Keys.ENTER)
            driver.implicitly_wait(10)
            time.sleep(2)
        except Exception as ex:
            print(ex)
            break
    driver.close()


def ministop_store():
    pass


def main():
    seven_eleven_store()
    emart_store()
    cu_store()
    gs25_store()


if __name__ == '__main__':
    main()
