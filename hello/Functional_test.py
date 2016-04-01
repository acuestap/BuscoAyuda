__author__ = 'Abimnelec Cuesta'
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        nombre = self.browser.find_element_by_id('name')
        nombre.send_keys('Abimelec')

        apellidos = self.browser.find_element_by_id('last_name')
        apellidos.send_keys('Cuesta')

        experiencia = self.browser.find_element_by_id('years_of_experience')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath(
            "//select[@id='job']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('phone_number')
        telefono.send_keys('30456876')

        correo = self.browser.find_element_by_id('email')
        correo.send_keys('acuestap@gmail.com')

        imagen = self.browser.find_element_by_id('imageFileUrl')
        imagen.send_keys('C:\Users\Public\Pictures\Sample Pictures\desierto.jpg')

        nombreUsuario = self.browser.find_element_by_id('username')
        nombreUsuario.send_keys('acuesta1')

        clave = self.browser.find_element_by_id('password')
        clave.send_keys('abc123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)
        span = self.browser.find_element(By.XPATH, '//span[text()="Abimelec Cuesta"]')

        self.assertIn('Abimelec Cuesta', span.text)