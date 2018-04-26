from selenium import webdriver

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\chromedriver.exe')
driver.implicitly_wait(15)
driver.get('https://www.soccer24.com/europe/champions-league/results/')

