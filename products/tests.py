import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


UserModel = get_user_model()

class TestProductList(APITestCase):
    def test_can_get_product_list(self):
        data = {"name": "FOOD1", "description": "","category":"http://localhost:8000/categories/2/"}
        url = reverse('list')
        response = self.client.get(url, data, format='Json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 8)

class TestProductDetail(APITestCase):
    @pytest.mark.django_db
    def test_can_get_product_detail(self):
        url = reverse('product_detail')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestUpdateProduct():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_updateProduct(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.find_element(By.XPATH, "//button[@type=\'button\']").click()
        self.driver.find_element(By.LINK_TEXT, "Noodels 1").click()
        self.driver.find_element(By.LINK_TEXT, "Update").click()
        element = self.driver.find_element(By.ID, "id_name")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "id_name")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "id_name")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "id_name").click()
        self.driver.find_element(By.ID, "id_name").send_keys("Noodels 2")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()


class TestCreateNewProduct():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_createNewProduct(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1141, 633)
        self.driver.find_element(By.XPATH, "//button[@type=\'button\']").click()
        self.driver.find_element(By.LINK_TEXT, "Add product").click()
        self.driver.find_element(By.ID, "id_name").click()
        self.driver.find_element(By.ID, "id_name").send_keys("Noodles")
        self.driver.find_element(By.ID, "id_description").click()
        self.driver.find_element(By.ID, "id_description").send_keys(
            "This is a new Product callled noodels under food Category")
        self.driver.find_element(By.ID, "id_category").click()
        dropdown = self.driver.find_element(By.ID, "id_category")
        dropdown.find_element(By.XPATH, "//option[. = 'Food']").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".pull-right").click()


class TestProductList2():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_productList(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1141, 633)
        self.driver.find_element(By.ID, "left-bar").click()
        self.driver.find_element(By.XPATH, "//button[@type=\'button\']").click()

