from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://nb.58.com/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&pts=1681365672334")
time.sleep(3)
#等待3秒
driver.set_window_size(600,800)
#自定义设置浏览器大小‘宽度’ ‘高度’                
driver.find_element(By.CSS_SELECTOR,"#commonTopbar_login > a:nth-child(1)").click()
time.sleep(3)
driver.find_element(By.ID,"mask_body_item_username").send_keys('13152753525')
time.sleep(3)
driver.find_element(By.ID,"mask_body_item_newpassword").send_keys('wang1215')
time.sleep(3)
driver.find_element(By.ID,"mask_body_item_login").click()
time.sleep(3)
driver.find_element(By.CLASS_NAME,"keyword").send_keys('租房')
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="searchbtn"]').click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,'#nav-container > ul > li.on > a').click()
time.sleep(3)
driver.find_element(By.CLASS_NAME,"strongbox").click()
