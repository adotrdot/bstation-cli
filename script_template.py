'''
Selenium WebDriver with python
'''

# LIBRARY
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# Make page load faster
options = Options()
options.page_load_strategy = 'eager'
options.headless = True

# Website url goes here
url = "url_here"

# Start firefox driver
driver = webdriver.Firefox(options=options)

# Open page
driver.get(url)

'''
Some shows have a page functionality that hides some episodes. To show them, we have to click some buttons.
Here, we check for those buttons.
To better understand these lines of code, inspect the bilibili.tv's pages.
'''
try:
    section = driver.find_element(By.CLASS_NAME, "swiper-with-auto-pivot.video-episodes__sections")
    btns = section.find_elements(By.CLASS_NAME, "scroll-list__item")
except:
    try:
        series = driver.find_element(By.CLASS_NAME, "swiper-with-auto-pivot.video-episodes__series")
        btns = []
    except:
        btns = driver.find_elements(By.CLASS_NAME, "scroll-list__item")

# Prepare write target
f = open(".bstation-cli.tmp", "w")

# If the number of buttons is more than or equal to 2, print the page source sequentially.
# Write and append them to f.
if len(btns) >= 2:
    f.write(driver.page_source)
    f.close()
    f = open(".bstation-cli.tmp", "a")
    for btn in btns[1:]:
        if btn.text != "PV&More":
            btn.click()
            f.write(driver.page_source)

# If no button is found, just print the page source and write it to f.
else:
    f.write(driver.page_source)

# Close write target and quit selenium
f.close()
driver.quit()
