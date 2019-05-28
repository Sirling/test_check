import random
import string
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Check:

    driver = webdriver.Chrome(executable_path="C:\\Work\\Projects\\test\\utilities\\drivers\\chromedriver.exe")
    driver.maximize_window()
    store_office = None
    name = "form_name"
    experience = "form_experienced"
    published = "form_published"
    delivery = "form_delivery"
    disability = "form_disability"
    contact1 = "form_contact_one"
    contact2 = "form_contact_two"
    manager_name = "form_manager_name"
    reward = "form_reward"
    form_title = "form_formTitle"
    start = "form_startAt"
    end = "form_endAt"
    responsibilities = "form_responcebilitiesTitle"
    requirements = "form_requirementsTitle"

    def auth(self):
        driver = self.driver

        driver.get("https://newsilpo.iir.fozzy.lan/admin")
        driver.find_element(By.ID, "username").send_keys("b.shvets")
        driver.find_element(By.ID, "password").send_keys("Ganjubas6")
        driver.find_element(By.ID, "domain").click()
        driver.find_element(By.CSS_SELECTOR, "#domain option:nth-child(4)").click()
        driver.find_element(By.CLASS_NAME, "button").click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "navbar-brand")))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "hide-button")))
        driver.find_element(By.CLASS_NAME, "hide-button").click()

    @classmethod
    def random_template(cls):

        cls.driver.find_element(By.CLASS_NAME, "select2-container").click()
        WebDriverWait(cls.driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#select2-form_template-results li")))
        templates_list = cls.driver.find_elements(By.CSS_SELECTOR, "#select2-form_template-results li")
        city = random.choice(templates_list)
        city.click()

    @classmethod
    def random_city(cls):

        cls.driver.find_element(By.ID, "select2-form_city-container").click()
        WebDriverWait(cls.driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#select2-form_city-results li")))
        cities_list = cls.driver.find_elements(By.CSS_SELECTOR, "#select2-form_city-results li")
        city = random.choice(cities_list)
        city.click()

    @classmethod
    def store_or_office(cls):
        store = cls.driver.find_element(By.ID, "form_type_0")
        office = cls.driver.find_element(By.ID, "form_type_1")
        if store.is_selected():
            cls.store_office = True
        elif office.is_selected():
            cls.store_office = False
        else:
            Check.select_random_type()
            Check.store_or_office()

    @classmethod
    def select_random_type(cls):
        store = cls.driver.find_element(By.ID, "form_type_0")
        office = cls.driver.find_element(By.ID, "form_type_1")
        type_list = [store, office]
        check = random.choice(type_list)
        check.click()

    @classmethod
    def random_store(cls):

        cls.driver.find_element(By.ID, "select2-form_store-container").click()
        WebDriverWait(cls.driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#select2-form_store-results li")))
        stores_list = cls.driver.find_elements(By.CSS_SELECTOR, "#select2-form_store-results li")
        store = random.choice(stores_list)
        store.click()

    @classmethod
    def random_office(cls):

        cls.driver.find_element(By.ID, "select2-form_office-container").click()
        WebDriverWait(cls.driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#select2-form_office-results li")))
        offices_list = cls.driver.find_elements(By.CSS_SELECTOR, "#select2-form_office-results li")
        offices = random.choice(offices_list)
        offices.click()

    @classmethod
    def random_rubric(cls):

        cls.driver.find_element(By.ID, "select2-form_rubric-container").click()
        WebDriverWait(cls.driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#select2-form_rubric-results li")))
        rubrics_list = cls.driver.find_elements(By.CSS_SELECTOR, "#select2-form_rubric-results li")
        rubric = random.choice(rubrics_list)
        rubric.click()

    @classmethod
    def random_category(cls):

        cls.driver.find_element(By.ID, "select2-form_category-container").click()
        WebDriverWait(cls.driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#select2-form_category-results li")))
        categories_list = cls.driver.find_elements(By.CSS_SELECTOR, "#select2-form_category-results li")
        category = random.choice(categories_list)
        category.click()

    @classmethod
    def random_employment(cls):
        partial = cls.driver.find_element(By.ID, "form_employment_0")
        full = cls.driver.find_element(By.ID, "form_employment_1")
        employment_list = [partial, full]
        check = random.choice(employment_list)
        check.click()

    @classmethod
    def random_checkbox_click(cls, locator):
        choice = random.getrandbits(1)
        if choice == 1:
            element = cls.driver.find_element(By.ID, locator)
            element.click()

        else:
            pass

    @classmethod
    def fill_field(cls, locator, text):
        element = cls.driver.find_element(By.ID, locator)
        element.clear()
        element.send_keys(text)

    @classmethod
    def random_digits(cls, n):
        return ''.join(random.choices(string.digits, k=n))

    @classmethod
    def random_id(cls):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=13))

    @classmethod
    def random_multiselect(cls):

        selector = cls.driver.find_element(By.CSS_SELECTOR, ".select2-selection--multiple")
        selector.click()
        multi_list = cls.driver.find_elements(By.CSS_SELECTOR, "#select2-form_pages-results li")
        for item in multi_list:
            rand = random.getrandbits(1)
            if rand == 1:
                item.click()
            else:
                pass

    def create_vacancy(self, quantity):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, ".sidebar-menu li:nth-child(21)").click()
        vacancies = driver.find_element(By.CSS_SELECTOR, "a[href='/admin/dictionary/hr_vacancy']")
        driver.execute_script("return arguments[0].scrollIntoView();", vacancies)
        vacancies.click()
        for i in range(21, quantity):
            add = driver.find_element(By.CSS_SELECTOR, "a[href='/admin/dictionary/hr_vacancy/add']")
            add.click()
            self.random_template()
            sleep(1)
            self.fill_field(self.name, "Вакансія {}".format(i))
            self.store_or_office()
            if self.store_office:
                self.random_city()
                sleep(1)
                self.random_store()
            elif not self.store_office:
                self.random_city()
                self.random_office()
                self.random_rubric()
                self.random_category()
            self.random_employment()
            self.random_checkbox_click(self.experience)
            driver.find_element(By.ID, self.published).click()
            self.random_checkbox_click(self.delivery)
            self.random_checkbox_click(self.disability)
            self.fill_field(self.contact1, self.random_digits(13))
            self.fill_field(self.contact2, self.random_digits(13))
            self.fill_field(self.manager_name, "Оксана")
            self.fill_field(self.reward, self.random_digits(5))
            self.fill_field(self.form_title, "Анкета")
            self.fill_field(self.start, "19.10.2018")
            self.fill_field(self.end, "19.10.2019")
            self.fill_field(self.responsibilities, "Обов'язки")
            self.fill_field(self.requirements, "Вимоги")
            self.random_multiselect()
            self.driver.find_element(By.CSS_SELECTOR, ".btn[type='submit']").click()
            self.driver.find_element(By.CSS_SELECTOR, "a[href='/admin/dictionary/hr_vacancy'").click()

        driver.close()
        driver.quit()

if __name__ == "__main__":
    Check().auth()
    Check().create_vacancy(600)
