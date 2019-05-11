from selenium import webdriver # This is the proper way to import webdriver
from selenium.webdriver.common.keys import Keys # This is so we can simulate key presses
from selenium.webdriver.chrome.options import Options # This is to configure Chrome options
from getpass import getpass # This is to prevent the password to be echoed to the terminal
from time import sleep
import sys  
sys.tracebacklimit = 0 # Supressing tracebacks, just so the terminal stays nice and clean

print()
print("UPS CampusShip tool".center(100, ' '))
print("Created by Giovanny Ramos".center(100, ' '))
print()
print("With this tool you can semi-automate the input of information on the UPS CampusShip website.")
print("You will still have to select the State, Packaging type and Shipping Service manually.")
print()

# Getting your login information
username = input("Enter Username: ")
username = username.strip()
pass_word = getpass("Enter password: ")
pass_word = pass_word.strip()
print()

# Shipping info starts here
Shipper = input("Enter your full name: ")
receiver = input("Name of receiver: ")
Rcity = input("Name of city: ")
Rcity = Rcity.upper()
Rzipcode = input("Enter zip code: ")
Raddress = input("Enter address of receiver: ")
rSuite = input("Enter suite, apt, unit, building etc (if none then leave blank): ")
LocNum = input("Enter location number: ")

# Chrome options 
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized") # Here we are adding the option to start the browser maximized

# Launching the web browser
browser = webdriver.Chrome('C:/ChromeDriver/chromedriver.exe', options=options)
browser.get('https://www.campusship.ups.com/login?reasonCode=-1')

user = browser.find_element_by_id('userid')
passW = browser.find_element_by_id('password')

# Entering log in info
user.send_keys(username)
passW.send_keys(pass_word)
passW.send_keys(Keys.ENTER)

# Page after successful login
try:
    newAddr = browser.find_element_by_link_text('Enter New Address')
    browser.implicitly_wait(5)
    newAddr.send_keys("\n") # good workaround for when you get a 'cannot click on element' error
except:
    browser.quit()
    print()
    print("Wrong log in information. Close the program and try again.")
    sleep(6)
    sys.exit()

# After clicking "Enter a New Address"
company = browser.find_element_by_id('shipToNameValue')
city = browser.find_element_by_id('shipToCityValue')
contact = browser.find_element_by_id('shipToContactNameValue')
zipcode = browser.find_element_by_id('shipToPostalValue')
address = browser.find_element_by_id('shipToStreetValue')
suite = browser.find_element_by_id('shipToAddr2Value')
cost_center = browser.find_element_by_id('reference_value1')
shippers_name = browser.find_element_by_id('reference_value2')

# Applying all the information provided to the proper field
company.send_keys('SP+')
city.send_keys(Rcity)
contact.send_keys(receiver)
zipcode.send_keys(Rzipcode)
address.send_keys(Raddress)
suite.send_keys(rSuite)
cost_center.send_keys(LocNum)
shippers_name.send_keys(Shipper)

