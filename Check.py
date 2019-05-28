from time import sleep
import cv2
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class Check:

    def test_check(self):
        capabilities = DesiredCapabilities()
        self.driver = webdriver.Chrome(executable_path="C:\\Work\\Projects\\test\\utilities\\drivers\\chromedriver.exe")
        self.driver.maximize_window()
        driver = self.driver

        driver.get('https://newsilpo.iir.fozzy.lan/gift-certificates')
        image = driver.find_element(By.CSS_SELECTOR, '.intro-colored').value_of_css_property('background-image')
        print(image)
        result = image[5:(len(image)-2)]
        print(result)
        im = cv2.imread('https://newsilpo.iir.fozzy.lan/uploads/2018/09/14/5b9bc5e2071e1.png')
        print(im)
        sleep(5)
        driver.close()
        driver.quit()

    def cert(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Work\\Projects\\test\\utilities\\drivers\\chromedriver.exe")
        self.driver.maximize_window()
        driver = self.driver

        driver.get('https://newsilpo.iir.fozzy.lan/gift-certificates')
        certificate =  driver.find_elements(By.CSS_SELECTOR, "div[class^='certificates-block-wrapper']")[0]
        print(certificate.get_attribute('class'))

if __name__ == "__main__":
    Check().cert()