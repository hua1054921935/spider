from selenium import webdriver

drive = webdriver.Chrome()
drive.get('http://www.cuiweijuxing.com/modules/article/search.php')
search = drive.find_element_by_name('searchkey')
search.send_keys('白洁')
submit = drive.find_element_by_name('submit')
submit.click()
# a=drive.find_element_by_class_name('c_subject')
url = drive.find_element_by_xpath('//span[@class="c_subject"]/a').get_attribute("href")

drive.close()
