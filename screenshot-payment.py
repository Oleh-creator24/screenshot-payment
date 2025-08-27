# screenshot-payment.py

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time
import os

def main():
    # Настройки Firefox
    options = Options()
    options.add_argument("--width=1280")
    options.add_argument("--height=800")

    # Если Selenium не видит Firefox, укажи путь к firefox.exe
    # options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

    # Используем webdriver-manager, чтобы автоматически скачать geckodriver
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

    try:
        # Открываем сайт
        driver.get("https://itcareerhub.de/ru")
        time.sleep(3)

        # Находим раздел "Способы оплаты"
        payment_section = driver.find_element(
            By.XPATH, "//h2[contains(text(),'Способы оплаты обучения')]/parent::div"
        )

        driver.execute_script("arguments[0].scrollIntoView();", payment_section)
        time.sleep(2)

        # Путь для сохранения скриншота
        screenshot_path = os.path.join(os.getcwd(), "payment_section.png")
        driver.save_screenshot(screenshot_path)
        print(f"✅ Скриншот сохранён: {screenshot_path}")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()

