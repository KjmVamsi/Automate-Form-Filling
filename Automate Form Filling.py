from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the web form page
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSf3uloEJJomFGJIM7kCjUbwSsiYq0BoSM6amsAL7ki3nWqsmQ/viewform?usp=sf_link')

# Allow the page to load
time.sleep(60)

# Fill out the form fields
driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',"vamsi").send_keys(person["name"])
driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input', "Vamsi@gmail.com").send_keys(person["email"])
driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea', "Male").send_keys(person["gender"])
driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input', "2003-01-01").send_keys(person["dob"])
driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input', "10000").send_keys(person["steps"])

# Submit the form
driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span', "submit").click()

# Allow time for the response to load
time.sleep(60)

# Print the response
response = driver.page_source
print(response)

# Close the browser
driver.quit()
