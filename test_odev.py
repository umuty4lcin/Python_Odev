from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date
import datetime


class Test_DemoClass:
    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))

    def scrennshot_for_product_purchase(self,username,password):
        self.driver.save_screenshot(f"{self.folderPath}/test_username_password_{username}-{password}-{datetime.datetime.now().microsecond}.png")

    def scrennshot(self,username,password):
        self.driver.save_screenshot(f"{self.folderPath}/test_username_password{username}-{password}.png")

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.quit()

    list_of_entry = [("1","1"),(" "," "),("username","password"),("null","null")]    
    @pytest.mark.parametrize("username,password",list_of_entry)
    def test_username_password(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        username_Input = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        password_Input = self.driver.find_element(By.ID,"password")

        username_Input.send_keys(username)
        password_Input.send_keys(password)

        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        self.scrennshot(username,password)
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service" 

    def test_password_null(self,username="1",password=""):
        self.waitForElementVisible((By.ID,"user-name"))
        username_Input = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        password_Input = self.driver.find_element(By.ID,"password")
        
        username_Input.send_keys(username)
        password_Input.send_keys(password)

        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        self.scrennshot(username,password)
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]")
        assert errorMessage.text == "Epic sadface: Password is required"
    
    def test_entry(self,username="standard_user",password="secret_sauce"):
        self.waitForElementVisible((By.ID,"user-name"))
        username_Input = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        password_Input = self.driver.find_element(By.ID,"password")

        username_Input.send_keys(username)
        password_Input.send_keys(password)

        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID,"login-button")
        self.scrennshot(username,password)
        loginBtn.click()
        
    
    def test_click_error_message(self,username="1",password="1"):
        self.waitForElementVisible((By.ID,"user-name"))
        username_Input = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        password_Input = self.driver.find_element(By.ID,"password")

        username_Input.send_keys(username)
        password_Input.send_keys(password)

        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        error_button = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button")
        error_button.click()
        self.scrennshot(username,password)
    
    def test_entry_webpage(self,username="standard_user",password="secret_sauce"):
        self.waitForElementVisible((By.ID,"user-name"))
        username_Input = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        password_Input = self.driver.find_element(By.ID,"password")

        username_Input.send_keys(username)
        password_Input.send_keys(password)

        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)
        self.scrennshot(username,password)
        
    
    def test_find_list_items(self,username="standard_user",password="secret_sauce"):
        self.waitForElementVisible((By.ID,"user-name"))
        username_Input = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        password_Input = self.driver.find_element(By.ID,"password")

        username_Input.send_keys(username)
        password_Input.send_keys(password)

        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        list_items = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        self.scrennshot(username,password)
        assert len(list_items) == 6

    def test_add_to_cart(self,username="standard_user",password="secret_sauce"):
        self.waitForElementVisible((By.ID,"user-name"))
        username_Input = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        password_Input = self.driver.find_element(By.ID,"password")

        username_Input.send_keys(username)
        password_Input.send_keys(password)

        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)

        button_addToCart = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        button_addToCart.click()
        self.scrennshot(username,password)

    def test_name_sorting_change(self,username="standard_user",password="secret_sauce"):
        self.waitForElementVisible((By.ID,"user-name"))
        username_Input = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        password_Input = self.driver.find_element(By.ID,"password")

        username_Input.send_keys(username)
        password_Input.send_keys(password)

        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        sorting_button = self.driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/div/span/select/option[2]")
        sorting_button.click()
        sleep(2)
        self.scrennshot(username,password)

    def test_product_purchase(self,username="standard_user",password="secret_sauce"):
        self.waitForElementVisible((By.ID,"user-name"))
        username_Input = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        password_Input = self.driver.find_element(By.ID,"password")

        username_Input.send_keys(username)
        password_Input.send_keys(password)

        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        button_addToCart = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket")
        button_addToCart.click()
        self.scrennshot_for_product_purchase(username,password)
        shopping_cart = self.driver.find_element(By.ID,"shopping_cart_container")
        shopping_cart.click()
        self.scrennshot_for_product_purchase(username,password)

        checkOut_button = self.driver.find_element(By.ID,"checkout")
        checkOut_button.click()
        self.scrennshot_for_product_purchase(username,password)

        firstName = self.driver.find_element(By.ID,"first-name")
        firstName.send_keys("test")

        lastName = self.driver.find_element(By.ID,"last-name")
        lastName.send_keys("test")

        zipCode = self.driver.find_element(By.ID,"postal-code")
        zipCode.send_keys("test")
        self.scrennshot_for_product_purchase(username,password)

        contiune_button = self.driver.find_element(By.ID,"continue")
        contiune_button.click()
        self.scrennshot_for_product_purchase(username,password)

        finish_button = self.driver.find_element(By.ID,"finish")
        finish_button.click()
        self.scrennshot_for_product_purchase(username,password)

        backHome_button = self.driver.find_element(By.ID,"back-to-products")
        backHome_button.click()




