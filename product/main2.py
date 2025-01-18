# import time
# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup

# driver_path = ChromeDriverManager().install()
# driver_path = '/'.join(driver_path.split('/')[:-1]) + '/chromedriver'
# os.chmod(driver_path, 0o755)

# options = Options()
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--headless")  # Optional

# driver = webdriver.Chrome(service=Service(driver_path), options=options)

# url = 'https://www.koupon.ai/'

# driver.get(url)
# soup = BeautifulSoup(driver.page_source, features='lxml')

# headings = soup.find_all("span")
# for heading in headings:
#     print(heading.getText())

# time.sleep(10)

# driver.quit()


from state import ApplicationState

app1 = ApplicationState()
