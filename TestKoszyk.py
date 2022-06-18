# BIBLIOTEKI
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# DANE TESTOWE
ilosc_alergia = '2'
nazwa_karmy = 'Purina'
ilosc_wyszukana = '3'

class Akceptacja_cookies(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')
        self.driver.get("https://zooart.com.pl/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def test_alergia(self):
        sleep(1)
        driver = self.driver
        cookies = driver.find_element(By.ID, "ckdsclmrshtdwn_v2")
        cookies.click()

        #Koty
        koty = driver.find_element(By.XPATH,'//a[@title="Koty"]')
        koty.click()

        #Karma dla kotów
        karma = driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div[1]/a[1]/span[1]')
        karma.click()

        #Karma weterynaryjna
        karma_vet = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[1]/a[2]/img')
        karma_vet.click()

        #Karma mokra
        karma_vet_mokra = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/a[2]/span[1]')
        karma_vet_mokra.click()

        #Alergie
        karma_vet_mokra_alergie = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[1]/a[1]/span[1]')
        karma_vet_mokra_alergie.click()

        karma_vet_mokra_alergie_1 = driver.find_element(By.XPATH, '//*[@id="search"]/div[2]/div/h3/a')
        karma_vet_mokra_alergie_1.click()

        #Wybranie ilości
        ilosc_karmy = driver.find_element(By.ID, "projector_number")
        ilosc_karmy.click()
        ilosc_karmy.send_keys(Keys.CONTROL + "a")
        ilosc_karmy.send_keys(Keys.DELETE)
        ilosc_karmy.send_keys(ilosc_alergia)

        #Dodaj do koszyka
        dodaj = driver.find_element(By.ID, 'projector_button_basket')
        dodaj.click()

        #Wyszukuję dowolną karmę
        wyszukaj = driver.find_element(By.XPATH, '//*[@id="menu_search_text"]')
        wyszukaj.click()
        wyszukaj.send_keys(nazwa_karmy)
        wyszukaj.send_keys(Keys.ENTER)

        #Wybiera pierwszy produkt z listy
        produkt = driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div/a/div/div')
        produkt.click()

        #Wybierz ilość
        wybierz_ilosc = driver.find_element(By.ID, "projector_number")
        wybierz_ilosc.click()
        wybierz_ilosc.send_keys(Keys.CONTROL + "a")
        wybierz_ilosc.send_keys(Keys.DELETE)
        wybierz_ilosc.send_keys(ilosc_wyszukana)

        dodaj = driver.find_element(By.ID, 'projector_button_basket')
        dodaj.click()

        #Przejście do koszyka i weryfikacja ilości produktów
        driver.find_element(By.XPATH, '//*[@id="menu_basket"]/span/span').click()

        karma_1 = driver.find_element(By.NAME, "set_quantity[1]").get_attribute("value")
        self.assertEqual(ilosc_alergia, karma_1)

        karma_2 = driver.find_element(By.NAME, "set_quantity[2]").get_attribute("value")
        self.assertEqual(ilosc_wyszukana, karma_2)

        #Opróźnij koszyk
        driver.find_element(By.XPATH, '//*[@id="basketedit_productslist"]/table/tbody/tr[6]/td/a[2]/i').click()

        #Zweryfikuj komunikat
        pusty_koszyk = driver.find_element(By.XPATH, '//*[@id="return_sub_basket_empty"]/h3').get_attribute("innerText")
        self.assertEqual("Twój koszyk jest pusty. Dodaj do niego towary, aby móc rozpocząć składanie zamówienia.", pusty_koszyk)



    def tearDown(self):
        sleep(5)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


