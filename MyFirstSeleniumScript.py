import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the URL for the web page
web_url = "https://hub.knime.com/"

# Start a webdriver instance
PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(web_url)
driver.maximize_window()
driver.implicitly_wait(20)

#find elements for accepting cookies
accept_cookies = driver.find_element(By.XPATH, "//button[@class='accept-button button primary']")
time.sleep(3)
accept_cookies.click()

#find elements for sign in button
sign_in_btn = driver.find_element(By.XPATH, "//button[@class='button primary compact']")
time.sleep(3)
sign_in_btn.click()

#find elements of username, password and submit button
username_field = driver.find_element(By.XPATH, "//input[@id='edit-name']")
password_field = driver.find_element(By.XPATH, "//input[@type='password']")
submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")

# Enter the credentials into the fields
username_field.send_keys("abhirajt7")
password_field.send_keys("MH01au6225")
time.sleep(3)
submit_btn.click()

#find element to click on profile
profile_icon = driver.find_element(By.XPATH, "//div[@class='avatar-placeholder avatar-missing placeholder']")
profile_icon.click()

#find element of user id and click on it
user_id = driver.find_element(By.XPATH, "//span[normalize-space(text())='abhirajt7']")
time.sleep(3)
user_id.click()

#find element for creating space
create_space = driver.find_element(By.XPATH, "//button[@class='button compact'][2]")
time.sleep(3)
create_space.click()

#find element to edit space name
space_name = driver.find_element(By.XPATH, "//textarea[@placeholder='Enter public space name']")
time.sleep(3)
space_name.send_keys("New space")

#find element to save the new space created
save_button = driver.find_element(By.XPATH, "//button[@class='function-button single primary']")
time.sleep(3)
save_button.click()

#find element to select more options
more_options = driver.find_element(By.XPATH, "//button[@class='toggle function-button single']")
more_options.click()

#find element to delete the space
delete_button = driver.find_element(By.XPATH, "//button[@class='modal-trigger button with-border compact']")
time.sleep(3)
delete_button.click()

#find element to enter the space name which is to be deleted
delete_space_name = driver.find_element(By.XPATH, "//input[@placeholder='space name']")
time.sleep(3)
delete_space_name.send_keys("New space")

#find element to click on delete button
delete_space_btn = driver.find_element(By.XPATH, "//button[@class='button primary fullWidth']")
time.sleep(3)
delete_space_btn.click()
time.sleep(3)

#Close the webdriver instance
driver.close()
