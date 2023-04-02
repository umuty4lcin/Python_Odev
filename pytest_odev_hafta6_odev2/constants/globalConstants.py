URL = "https://www.saucedemo.com/"

error_text = "Epic sadface: Username and password do not match any user in this service"
error_message_path = "//*[@id='login_button_container']/div/form/div[3]"
error_button_off_path = "//*[@id='login_button_container']/div/form/div[3]/h3/button"
error_message_lockedOut = "Epic sadface: Sorry, this user has been locked out."

excel_path = "data/invalid_login.xlsx"
sheet_number = "Sheet1"

username_ID = "user-name"
password_ID = "password"
loginbutton_ID = "login-button"

standart_user = "standard_user"
locked_out_user = "locked_out_user"
problem_user = "problem_user"
problem_user_img_xpath = "//*[@id='item_4_img_link']/img"
checkout_error_xpath = "//*[@id='checkout_info_container']/div/form/div[1]/div[4]"
checkout_error_message = "Error: Last Name is required"

secret_sauce = "secret_sauce"

sorting_button_xpath = "//*[@id='header_container']/div[2]/div/span/select"
sorting_az_Name_xpath = "//*[@id='header_container']/div[2]/div/span/select/option[1]"
sorting_za_Name_xpath = "//*[@id='header_container']/div[2]/div/span/select/option[2]"
sorting_lowToHigh_xpath = "//*[@id='header_container']/div[2]/div/span/select/option[3]"
sorting_highToLow_xpath = "//*[@id='header_container']/div[2]/div/span/select/option[4]"

sorting_option = [sorting_az_Name_xpath,sorting_za_Name_xpath,sorting_lowToHigh_xpath,sorting_highToLow_xpath]

menu_button_ID = "react-burger-menu-btn"
logout_bar_ID = "logout_sidebar_link"

twitter_icon_xpath = "//*[@id='page_wrapper']/footer/ul/li[1]/a"
linkedin_icon_xpath = "//*[@id='page_wrapper']/footer/ul/li[3]/a"
facebook_icon_xpath = "//*[@id='page_wrapper']/footer/ul/li[2]/a"

social_media_links = [twitter_icon_xpath,linkedin_icon_xpath,facebook_icon_xpath]

list_items_ClassName = "inventory_item"
list_ClassName = "inventory_list"

addToC_backBack_ID = "add-to-cart-sauce-labs-backpack"
addToC_bikeLight_ID = "add-to-cart-sauce-labs-bike-light"
addToC_tShirt_ID = "add-to-cart-sauce-labs-bolt-t-shirt"
addToC_jacket_ID = "add-to-cart-sauce-labs-fleece-jacket" 
addToC_onesie_ID = "add-to-cart-sauce-labs-onesie"
addToC_RedTshirt_ID = "add-to-cart-test.allthethings()-t-shirt-(red)"

list_of_items_ID = [
addToC_backBack_ID ,
addToC_bikeLight_ID,
addToC_tShirt_ID, 
addToC_jacket_ID, 
addToC_onesie_ID,
addToC_RedTshirt_ID]

item0_link_xpath = "//a[@id=\'item_0_title_link\']/div"
item1_link_xpath = "//a[@id=\'item_1_title_link\']/div"
item2_link_xpath = "//a[@id=\'item_2_title_link\']/div"
item3_link_xpath = "//a[@id=\'item_3_title_link\']/div"
item4_link_xpath = "//a[@id=\'item_4_title_link\']/div"
item5_link_xpath = "//a[@id=\'item_5_title_link\']/div"
back_to_products_ID = "back-to-products"

items_links_xpaths = [
item0_link_xpath,
item1_link_xpath,
item2_link_xpath,
item3_link_xpath,
item4_link_xpath,
item5_link_xpath
]

shopping_cart_link_xpath = "//*[@id='shopping_cart_container']/a" 
removeButton_bike_light_ID ="remove-sauce-labs-bike-light" 
checkoutButton_ID = "checkout"

checkout_info_xpath = "//*[@id='checkout_info_container']/div/form/div[1]"
firstname_ID = "first-name"
lastName_ID = "last-name"
postalCode_ID = "postal-code"

checkout_page_list = [
firstname_ID, 
lastName_ID,
postalCode_ID
]

continueButton_ID = "continue"
finishButton_ID = "finish"
backHomeButton_ID = "back-to-products"