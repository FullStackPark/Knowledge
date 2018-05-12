#!/usr/bin/python
# -*- coding:UTF-8 -*-
from datetime import datetime
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


# 定义截图函数
def snap_shot(url, image_path, scroll_top=90):

    # 打开页面，窗口最大化
    driver.get(url)
    driver.maximize_window()

    # 调用JS脚本滚动页面
    scroll_js = "var q=document.documentElement.scrollTop={}".format(scroll_top)
    driver.execute_script(scroll_js)

    # 截图存储
    driver.save_screenshot(image_path)


# 定义抠图函数
def crop_image(image_path, pattern_xpath, crop_path, scroll_top=90):

    # 获取页面元素及其位置、尺寸
    element = driver.find_element_by_xpath(pattern_xpath)
    location = element.location
    size = element.size

    # 计算抠取区域的绝对坐标
    left = location['x']
    top = location['y'] - scroll_top
    right = location['x'] + size['width']
    bottom = location['y'] + size['height'] - scroll_top

    # 打开图片，抠取相应区域并存储
    im = Image.open(image_path)
    im = im.crop((left, top, right, bottom))

    im.save(crop_path)



# 获取当前时间戳
now = datetime.now()
now_sign = str(now.day)+str(now.hour)+str(now.minute)+str(now.second)

print(now_sign)

# 启动截图函数，获取当前页面
snap_shot_path_1 = "snap_shot/maoyan_{0}_{1}.png".format('1', now_sign)
snap_shot_path_2 = "snap_shot/maoyan_{0}_{1}.png".format('2', now_sign)

snap_shot(url, snap_shot_path_1, scroll_top=90)
snap_shot(url, snap_shot_path_2, scroll_top=720)


# 启动抠图函数
for i in range(1,12):
    pattern = ".//*[@id='ticket_tbody']/ul[{}]/li[2]/b/i".format(i)
    crop_path = "snap_shot/crop/current_piaofang_{}.png".format(movie_names[i-1])
    crop_image(snap_shot_path_1, pattern, crop_path, scroll_top=90)

for i in range(13,24):
    pattern = ".//*[@id='ticket_tbody']/ul[{}]/li[2]/b/i".format(i)
    crop_path = "snap_shot/crop/current_piaofang_{}.png".format(movie_names[i-1])
    crop_image(snap_shot_path_2, pattern, crop_path, scroll_top=720)