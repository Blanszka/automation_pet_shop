#BIBLIOTEKI
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#DANE TESTOWE
email_test='test.mail@@.pl'
imie = 'Anna'
nazwisko = 'Kowalska'
ulica_numer = "Kocia 5/34"
kod_pocztowy = "02-300"
miasto = "Piesłowo"
haslo = "Tester123!"
telefon = "111 222 333"
login = "KocieSmaczki"
newsletter = "tak"

class ZooArt_Formularz(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')
        self.driver.get("https://zooart.com.pl/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)


    def test_formularz_bledny_mail(self):
        sleep(3)
        driver = self.driver
        cookies = driver.find_element(By.ID, "ckdsclmrshtdwn_v2")
        cookies.click()

        konto = driver.find_element(By.XPATH, "//i[@class='icon-user']")
        konto.click()

        rejestracja = driver.find_element(By.XPATH, "//a[@class='btn signin-form_register2']")
        rejestracja.click()

        # Uzupełnienie formularza - Osoba prywatna
        driver.find_element(By.ID, "client_type2").click()

        client_firstname = driver.find_element(By.XPATH,'//input[@name="client_firstname"]')
        client_firstname.send_keys(imie)

        client_lastname = driver.find_element(By.XPATH, '//input[@name="client_lastname"]')
        client_lastname.send_keys(nazwisko)

        client_street = driver.find_element(By.XPATH, '//input[@name="client_street"]')
        client_street.send_keys(ulica_numer)

        client_zipcode = driver.find_element(By.XPATH, '//input[@name="client_zipcode"]')
        client_zipcode.send_keys(kod_pocztowy)

        client_city = driver.find_element(By.XPATH, '//input[@name="client_city"]')
        client_city.send_keys(miasto)

        client_email = driver.find_element(By.XPATH, '//input[@name="client_email"]')
        client_email.send_keys(email_test)

        client_phone = driver.find_element(By.XPATH, '//input[@name="client_phone"]')
        client_phone.send_keys(telefon)

        #Dane do dostawy = adres dostawy
        driver.find_element(By.ID, "deliver_to_billingaddr1").click()

        delivery_firstname = driver.find_element(By.ID, "delivery_firstname").get_attribute("value")
        self.assertEqual(imie, delivery_firstname)

        delivery_lastname = driver.find_element(By.ID, "delivery_lastname").get_attribute("value")
        self.assertEqual(nazwisko, delivery_lastname)

        delivery_street = driver.find_element(By.ID, "delivery_street").get_attribute("value")
        self.assertEqual(ulica_numer, delivery_street)

        delivery_zipcode = driver.find_element(By.ID, "delivery_zipcode").get_attribute("value")
        self.assertEqual(kod_pocztowy, delivery_zipcode)

        delivery_city = driver.find_element(By.ID, "delivery_city").get_attribute("value")
        self.assertEqual(miasto, delivery_city)

        delivery_phone = driver.find_element(By.ID, "delivery_phone").get_attribute("value")
        self.assertEqual(telefon, delivery_phone)

        client_login = driver.find_element(By.XPATH, '//input[@name="client_login"]')
        client_login.send_keys(login)

        client_password = driver.find_element(By.XPATH, '//input[@name="client_password"]')
        client_password.send_keys(haslo)

        repeat_password = driver.find_element(By.XPATH, '//input[@name="repeat_password"]')
        repeat_password.send_keys(haslo)
        #CZY CHCĘ NEWSLETTER
        if newsletter == "tak":
            driver.find_element(By.XPATH, '//button[@class="btn fbs02checkAll"]').click()
        else:
            driver.find_element(By.ID, "terms_agree").click()

        rejestruj_konto = driver.find_element(By.XPATH, '//button[@id="submit_clientnew_form"]')
        rejestruj_konto.click()
        #KOMUNIKAT O BŁĘDNYM ADRESIE EMAIL
        error_message = driver.find_element(By.XPATH,'//div[@class="menu_messages_warning_sub"]/p').get_attribute("innerText")
        self.assertEqual("Adres e-mail jest błędny.", error_message)

    def tearDown(self):
        sleep(3)
        self.driver.quit()

if __name__=="__main__":
    unittest.main()
