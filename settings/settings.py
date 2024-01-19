from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import   Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display



import time



service = Service(ChromeDriverManager().install())
# Set ChromeOptions() 
options = webdriver.ChromeOptions() 


# Add the proxy as argument 


driver = webdriver.Chrome(options=options, service=service)

# Input Values
url = 'https://scotlis.ros.gov.uk/'
inputValue = 'AB159NH'

# Page Objects - Page Default
radioOption = '//*[@id="search-form-radios-2"]'
inputPath = '//*[@id="searchTerm"]'
searchButton = '//*[@id="home-search-button"]'

# Page Objects - Page from input Value
firstlink = '//*[@id="main-content"]/table/tbody/tr[1]/td[1]/a'

# Page Objects - Page from selected register
pageElements = {
'titleNumberElement':'//*[@id="property-details-title-number"]',
'addressElement': '//*[@id="property-details-address"]',
'lastPurchasePriceElement' : '//*[@id="property-details-last-purchase-price"]',
'lastPurchaseDateElement' : '//*[@id="property-details-last-purchase-date"]',
'landRegister': '//*[@id="property-details-land-register-status"]',
'interestElement' : '//*[@id="property-details-interest"]',
'propertyTypeElement': '//*[@id="property-details-property-type"]',
'purchaseDate': '//*[@id="property-prices-purchase-date-0"]',
'priceElement' : '//*[@id="property-prices-purchase-price-0"]'
}

def site(url,insertValue, timeout=10):
    driver.get(url)

    driver.find_element('xpath', radioOption).click()
    driver.find_element('xpath', inputPath).send_keys(insertValue)
    driver.find_element('xpath', searchButton).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, firstlink)))
    driver.find_element('xpath', firstlink).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,pageElements['titleNumberElement'])))

    for element in pageElements.values():
        elementContent = driver.find_element('xpath', element)
        elementValue = elementContent.text
        print (elementValue)


    time.sleep(5)



teste = site(url, inputValue)