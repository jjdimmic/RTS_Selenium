#author: Jonathan Dimmick

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

print("Test Automation Excersize")
print("==========================")
print("==========================/n/n")


print("TEST 1: Verify Google site can be reached")
driver = webdriver.Chrome(service_log_path='./logs/log.log')
try:
    driver.get("http://www.google.com")
    print("TEST PASSED")
except:
    print("Google site could not be reached")
    print("TEST FAILED")

print("TEST 2: Verify Google Site has a Search box")
try:
    searchBox = driver.find_element(By.NAME,"q")
    print("TEST PASSED")
except:
    print("Search Box field not found")
    print("TEST FAILED")
    

print("TEST 3: Verify Search Box works")
try:
    searchBox.clear()
    searchBox.send_keys("RTS Labs")
    searchBox.send_keys(Keys.RETURN)
    results_pg1 = driver.find_element(By.ID, "rso")
    print("TEST PASSED")
except:
    print("Search box search was unsuccessful")
    print("TEST FAILED")  
    
print("TEST 4: Click first search result link")
try:
    results_pg1.find_element(By.XPATH, '//*/h3').click()
    print("TEST PASSED")
except:
    print("First link in results failed to be clicked")
    print("TEST FAILED")    

print("==========================")
print("TEST ENDED")

sleep(5)
driver.close()