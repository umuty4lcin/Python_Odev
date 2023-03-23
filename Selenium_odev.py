from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_Saucedemo:
    def username_password_null(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        username_input = driver.find_element(By.ID,"user-name")
        password_input = driver.find_element(By.ID,"password")
        sleep(2)
        
        username_input.send_keys(" ")
        password_input.send_keys(" ")
        sleep(1)

        login_button = driver.find_element(By.ID,"login-button")
        sleep(1)
        login_button.click()
        error_message = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]")
        test_result = error_message.text == "Epic sadface: Username and password do not match any user in this service"
        if test_result == True:
            print("\nEpic sadface: Username and password do not match any user in this service")
        else:
            pass
        sleep(3)

    def only_password_null(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        username_input = driver.find_element(By.ID,"user-name")
        password_input = driver.find_element(By.ID,"password")
        sleep(2)
        
        username_input.send_keys("1")
        password_input.send_keys(" ")
        sleep(1)

        login_button = driver.find_element(By.ID,"login-button")
        sleep(1)
        login_button.click()
        error_message = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]")
        test_result = error_message.text == "Epic sadface: Password is required"
        if test_result == True:
            print("\nEpic sadface: Password is required")
        else:
            pass
        sleep(3)

    def accepted_information(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        username_input = driver.find_element(By.ID,"user-name")
        password_input = driver.find_element(By.ID,"password")
        sleep(2)
        
        username_input.send_keys("locked_out_user")
        password_input.send_keys("secret_sauce")
        sleep(1)

        login_button = driver.find_element(By.ID,"login-button")
        sleep(1)
        login_button.click()
        error_message = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]")
        test_result = error_message.text == "Epic sadface: Sorry, this user has been locked out."
        if test_result == True:
            print("\nEpic sadface: Sorry, this user has been locked out.")
        else:
            pass
        sleep(3)
    
    def click_error_message(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        username_input = driver.find_element(By.ID,"user-name")
        password_input = driver.find_element(By.ID,"password")
        sleep(2)
        
        username_input.send_keys("1")
        password_input.send_keys("1")
        sleep(1)

        login_button = driver.find_element(By.ID,"login-button")
        sleep(1)
        login_button.click()
        error_button = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button")
        sleep(3)
        error_button.click()
        sleep(5)
    
    def entry_webpage(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        username_input = driver.find_element(By.ID,"user-name")
        password_input = driver.find_element(By.ID,"password")
        sleep(2)
        
        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        sleep(1)

        login_button = driver.find_element(By.ID,"login-button")
        sleep(1)
        login_button.click()
        sleep(5)

    def find_list_items(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        username_input = driver.find_element(By.ID,"user-name")
        password_input = driver.find_element(By.ID,"password")
        sleep(2)
        
        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        sleep(1)

        login_button = driver.find_element(By.ID,"login-button")
        sleep(1)
        login_button.click()
        sleep(10)

        list_items = driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"\nListedeki ürün sayisi : {len(list_items)}")
    
test_class = Test_Saucedemo()
test_class.username_password_null()
test_class.only_password_null()
test_class.accepted_information()
test_class.click_error_message()
test_class.entry_webpage()
test_class.find_list_items()