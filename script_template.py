from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.page_load_strategy = 'eager'
options.headless = True

url = "url_here"

driver = webdriver.Firefox(options=options)

driver.get(url)

try:
    section = driver.find_element(By.CLASS_NAME, "swiper-with-auto-pivot.video-episodes__sections")
    btns = section.find_elements(By.CLASS_NAME, "scroll-list__item")
except:
    btns = driver.find_elements(By.CLASS_NAME, "scroll-list__item")

f = open(".bstation-cli.tmp", "w")

if len(btns) >= 2:
    f.write(driver.page_source)
    f.close()
    f = open(".bstation-cli.tmp", "a")
    for btn in btns[1:]:
        btn.click()
        f.write(driver.page_source)
else:
    f.write(driver.page_source)

f.close()
driver.quit()
