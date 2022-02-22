from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser= webdriver.Chrome(options=options) #창 최대화

url="https://m-flight.naver.com/"
browser.get(url)


browser.find_element_by_class_name("tabContent_option__2y4c6 select_Date__1aF7Y").click()