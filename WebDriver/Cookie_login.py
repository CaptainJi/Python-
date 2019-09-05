from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')

driver.add_cookie({'name':"BAIDUID",'value':'310755609A22C43D1874EEDF1474EA02:FG=1'})
driver.add_cookie({'name':"UBI",'value':'fi_PncwhpxZ%7ETaKAaviVwJBgFRsFE1O9uMxpKxs2GyPQUfWZoozs1GFajErgqL8jeGtPP2i-otHTVoTlP2-FoSjOgy%7EGWPIBicKnviOKRd23hZFzQfTfEyMUqON5dNNBPTNLj5jbVO2aNrpWT972jBzE2Vn'})

driver.refresh()