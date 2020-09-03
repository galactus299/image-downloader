import os
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
product=input("enter url  ")
driver = webdriver.Chrome(executable_path=r"C:/Program Files (x86)/chromedriver_win32/chromedriver.exe")
driver.get(product)
soup_level1=BeautifulSoup(driver.page_source, 'lxml')
list1=soup_level1.find_all("img")
for image in list1:
    try:
        url="http://www.nikon.pk"+image['src']
        r=requests.get(url,allow_redirects=True)
        name=os.path.basename(url)
        open(name, 'wb').write(r.content)
    except :
        continue

#list1=driver.find_element_by_tag_name("img")
#print(list1['scr'])