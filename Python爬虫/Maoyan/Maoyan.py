from selenium import webdriver
from PIL import Image

driver = webdriver.Firefox() # 创建webdriver对象

# url = "http://piaofang.maoyan.com" # 定义目标url

url = "http://piaofang.maoyan.com/?ver=normal"

driver.get(url) # 打开目标页面

# 获取当前电影名称列表
movie_names = [driver.find_element_by_xpath(".//*[@id='ticket_tbody']/ul[{}]/li[1]/b".format(i)).text for i in range(1,24)]

# 获取实时票房列表
current_piaofang = [driver.find_element_by_xpath(".//*[@id='ticket_tbody']/ul[{}]/li[2]/b/i".format(i)).text for i in range(1,24)]