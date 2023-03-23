#odev2

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SauceDemo:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    loginBtn = driver.find_element(By.ID, "login-button")

    def userAndPwNull(self): #Epic sadface: Username is required
         self.loginBtn.send_keys(Keys.ENTER)
         errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3").text
         print(f"Hata mesaji: {errorMessage}")

    def pwNull(self): #Epic sadface: Password is required
         self.username.send_keys("standard_user")
         self.loginBtn.send_keys(Keys.ENTER)
         errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3").text
         print(f"Hata mesaji: {errorMessage}")

    def lockedUser(self): #Epic sadface: Sorry, this user has been locked out.
         self.username.send_keys("locked_out_user")
         self.password.send_keys("secret_sauce")
         self.loginBtn.send_keys(Keys.ENTER)
         errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3").text
         print(f"Hata mesaji: {errorMessage}")

    def redXIcon(self): #closedXIcon
         self.loginBtn.send_keys(Keys.ENTER)
         errorBtn = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3/button")
         sleep(2)
         errorBtn.send_keys(Keys.ENTER)

    def successfulLogin(self): #/inventory.html
         self.username.send_keys("standard_user")
         self.password.send_keys("secret_sauce")
         self.loginBtn.send_keys(Keys.ENTER)
         items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
         print(f"Urun sayisi: {len(items)}")

sauceDemo = SauceDemo()
#test fonksiyonları teker teker calistirilmalidir!!!
sauceDemo.userAndPwNull()
#sauceDemo.pwNull()
#sauceDemo.lockedUser()
#sauceDemo.redXIcon()
#sauceDemo.successfulLogin()
