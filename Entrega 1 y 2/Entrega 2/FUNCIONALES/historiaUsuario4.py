# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestHistoriaUsuario4():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_historiaUsuario4(self):
    self.driver.get("https://pascualbravo.ingejei.com/cart/")
    self.driver.set_window_size(697, 703)
    element = self.driver.find_element(By.CSS_SELECTOR, ".has-color2-color > .current-menu-item .wp-block-navigation-item__label")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.LINK_TEXT, "Proceder al pago").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").click()
    element = self.driver.find_element(By.ID, "email")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("kvalencia373@gmail.com")
    self.driver.find_element(By.ID, "billing-first_name").click()
    self.driver.find_element(By.ID, "billing-first_name").send_keys("karen")
    dropdown = self.driver.find_element(By.ID, "billing-country")
    dropdown.find_element(By.XPATH, "//option[. = 'Colombia']").click()
    self.driver.find_element(By.ID, "billing-last_name").send_keys("perez")
    self.driver.find_element(By.ID, "billing-address_1").send_keys("calle 56")
    self.driver.find_element(By.ID, "billing-city").send_keys("Medellin")
    dropdown = self.driver.find_element(By.ID, "billing-state")
    dropdown.find_element(By.XPATH, "//option[. = 'Selecciona un departamento']").click()
    self.driver.find_element(By.ID, "billing-phone").send_keys("+574567678")
    self.driver.find_element(By.ID, "billing-state").click()
    dropdown = self.driver.find_element(By.ID, "billing-state")
    dropdown.find_element(By.XPATH, "//option[. = 'Antioquia']").click()
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    self.driver.find_element(By.CSS_SELECTOR, ".wc-block-checkout__no-payment-methods-notice").click()
    self.driver.find_element(By.CSS_SELECTOR, ".wc-block-components-button").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".wc-block-components-button")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".wc-block-checkout__no-payment-methods-notice > .wc-block-components-notice-banner__content").click()
  
