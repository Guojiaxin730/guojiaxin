from selenium import webdriver
options=webdriver.ChromeOptions()

options.add_argument('--ignore-certificate-errors')

driver=webdriver.Chrome(chrome_options=options)

driver.get(u'https://python.org/')

driver.close()
