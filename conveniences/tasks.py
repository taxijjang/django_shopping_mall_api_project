import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


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
    from .models import Product
    BASE_URL = "https://www.7-eleven.co.kr"
    seven_eleven_store_url = f"{BASE_URL}/product/presentList.asp"
    driver = get_driver()
    driver.get(seven_eleven_store_url)
    # time.sleep(5)

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
        # element = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located(
        #         (By.CSS_SELECTOR, f"#actFrm > div.cont_body > div.wrap_tab > ul > li:nth-child({value}) > a"))
        # )
        element = driver.find_element(By.CSS_SELECTOR,
                                      f"#actFrm > div.cont_body > div.wrap_tab > ul > li:nth-child({value}) > a")
        time.sleep(2)
        element.click()
        time.sleep(2)
        try:
            while True:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#listUl > li.btn_more > a'))
                )
                # element = driver.find_element(By.CSS_SELECTOR, '#listUl > li.btn_more > a')
                time.sleep(2)
                element.click()
                time.sleep(2)

        except Exception:
            print("모든 상품 페이지 스크롤 완료")

        for product in driver.find_elements(By.CSS_SELECTOR, '#listUl > li > div'):
            title, price = product.text.split('\n')
            image = f"{BASE_URL}{BeautifulSoup(product.get_attribute('innerHTML'), 'html.parser').find('img').get('src')}"
            print(sale_type, title, price, image)
            seven_eleven_products.append(
                Product.objects.get_or_create(
                    conveniences_store=Product.SEVEN_ELEVEN,
                    title=title,
                    price=int(price.replace(',', '')),
                    image=image,
                    sale_type=sale_type,
                ),
            )


if __name__ == '__main__':
    seven_eleven_store()

# javascript: fncMore('1');
