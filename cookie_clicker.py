from selenium import webdriver
import time

driver = webdriver.Edge(
    executable_path=r"C:\Program Files\Development\MicrosoftWebDriver.exe")

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie_clicker = driver.find_element_by_id("cookie")

start = time.time()


while (time.time() - start) < 300:
    cookie_clicker.click()
    if time.time() - start > 5:
        time.sleep(5)
        start = time.time()


cookie_counter = driver.find_element_by_id("money")
print(f"Your final score is: {cookie_counter.text}")
driver.quit()
