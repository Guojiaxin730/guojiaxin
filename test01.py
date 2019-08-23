from selenium import webdriver
from time import sleep, ctime
from selenium.common.exceptions import NoSuchElementException

#进入登陆界面，隐式等待

driver = webdriver.Chrome() 
driver.implicitly_wait(10)
driver.get("http://106.15.234.64")
try:
    print(ctime())
    driver.find_element_by_css_selector('[type="tel"]').send_keys("superadmin")
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())


#测试右侧页面元素显式等待
print(ctime())
for i in range(10):
    try:
        el = driver.find_element_by_class_name("login_right")
        if el.is_displayed():
            break
    except:
        pass
    sleep(1)
else:
    print("time out")
print(ctime())



#登陆页面，打印差异信息，作为自动化的断言点

print('Before search=======')

title = driver.title
print("title:"+title)

now_url = driver.current_url
print("URL:"+now_url)


pages=driver.find_element_by_class_name("login_btn")
driver.execute_script("arguments[0].click();", pages)

print('After search========')

title = driver.title
print("title:"+title)

now_url = driver.current_url
print("URL:"+now_url)
