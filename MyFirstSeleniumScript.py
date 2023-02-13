from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the URL for the login page
login_url = "https://hub.knime.com/"

# Set the credentials for the login process
username = "your_username"
password = "your_password"

# Start a webdriver instance
PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(login_url)

#find elements for accepting cookies
accept_cookies = driver.find_element(By.XPATH, "//button[@class='accept-button button primary']")
accept_cookies.click()

#find elements for sign in button
sign_in_btn = driver.find_element(By.XPATH, "//button[@class='button primary compact']")
sign_in_btn.click()

username_field = driver.find_element(By.XPATH, "//input[@id='edit-name']")
password_field = driver.find_element(By.XPATH, "//input[@type='password']")
submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")

# Enter the credentials into the fields
username_field.send_keys("abhirajt7")
password_field.send_keys("MH01au6225")
submit_btn.click()

profile_icon = driver.find_element(By.XPATH, "//div[@class='avatar-placeholder avatar-missing placeholder']")
profile_icon.click()

user_id = driver.find_element(By.XPATH, "//span[normalize-space(text())='abhirajt7']")
user_id.click()

create_space = driver.find_element(By.XPATH, "//button[@class='button compact'][2]")
create_space.click()

space_name = driver.find_element(By.XPATH, "//textarea[@placeholder='Enter public space name']")
space_name.click()

save_button = driver.find_element(By.XPATH, "//button[@class='function-button single primary']")
save_button.click()

more_options = driver.find_element(By.XPATH, "//button[@class='toggle function-button single']")
more_options.click()

delete_button = driver.find_element(By.XPATH, "//button[@class='modal-trigger button with-border compact']")
delete_button.click()

delete_space_name = driver.find_element(By.XPATH, "//input[@placeholder='space name']")
delete_space_name.send_keys("New space 4")

delete_space_btn = driver.find_element(By.XPATH, "//button[@class='button primary fullWidth']")
delete_space_btn.click()

#Close the webdriver instance
driver.close()
