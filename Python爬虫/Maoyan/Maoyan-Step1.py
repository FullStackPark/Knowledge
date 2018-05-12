#!/usr/bin/python
# -*- coding:UTF-8 -*-
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from PIL import Image # PIL 安装https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00140767171357714f87a053a824ffd811d98a83b58ec13000

# export PATH=$PATH:~/Documents/ExecutableApp/geckodriver

# export PATH=$PATH:~/Documents/ExecutableApp/geckodriver
# https://stackoverflow.com/questions/40073548/python-selenium-in-ubuntu-oserror-errno-20-not-a-directory
# driver = webdriver.Firefox() # 创建webdriver对象

# url = "http://piaofang.maoyan.com" # 定义目标url
# driver = webdriver.Firefox() # 创建webdriver对象
opts = FirefoxOptions()
opts.add_argument("--headless")

driver = webdriver.Firefox(executable_path='/Users/lw/Documents/ExecutableApp/geckodriver',options=opts)
url = "http://piaofang.maoyan.com/?ver=normal"

driver.get(url) # 打开目标页面

# 获取当前电影名称列表
movie_names = [driver.find_element_by_xpath(".//*[@id='ticket_tbody']/ul[{}]/li[1]/b".format(i)).text for i in range(1,24)]



s = str(movie_names).replace('u\'','\'')
print s.decode("unicode-escape")

print(movie_names)


# 获取实时票房列表
current_piaofang = [driver.find_element_by_xpath(".//*[@id='ticket_tbody']/ul[{}]/li[2]/b/i".format(i)).text for i in range(1,24)]

# 获取实时票房列表
current_piaofang = [driver.find_element_by_xpath(".//*[@id='ticket_tbody']/ul[{}]/li[2]/b/i".format(i)).text for i in range(1,24)]

s = str(current_piaofang).replace('u\'','\'')
print s.decode("unicode-escape")

print(current_piaofang)
