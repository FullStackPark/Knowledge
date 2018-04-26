#!/usr/bin/python 36
# -*- coding:utf-8 -*-

from time import sleep
import os,requests,random
from bs4 import BeautifulSoup

def get_chapterlist(url):
    # 获取页面上的所有章节名和章节的网址,生产一个dict来保存.然后返回
    html_data = requests.get(url)
    soup = BeautifulSoup(html_data.text,'lxml')
    chapterlist_data = soup.find('div',{'id': 'chapterlistload'})
    chapterlist = chapterlist_data.find_all('a',{'class':'ib'})
    chapter_dict = {}
    for chapter in chapterlist:
        chapter_name = chapter.text
        chapter_url = chapter.get('href')
        chapter_dict[chapter_name] = chapter_url
    return  chapter_dict

def get_chapterdetail(chapter_name,chapter_url):
    # 遍历取出章节名,网址,依次打开页面,获取图片的网址,下载保留图片
    # for chapter in chapter_dict:
    #   chapter_name = chapter
    #   chapter_url = chapter_url
    page_num = 1
    while True:
        if page_num > 1:
            new_url = 'http://www.tuku.cc'+chapter_url+'p'+str(page_num)+'/'
        else:
            new_url = 'http://www.tuku.cc'+chapter_url
        print(page_num, new_url)
        if requests.get(new_url).status_code == 200:
            # 状态码如果为200, 就是有正常的图片.不然就是图片没有了,可以退出
            html_data = requests.get(new_url)
            soup = BeautifulSoup(html_data.text,'lxml')
            img_url = soup.find('img',{'id': 'cp_image'}).get('src')
            img_name = img_url.split('/')[-1]
            print(img_url,img_name)
            # 如果获取地址为空, 就是章节没有了, 退出这个环节
            if not len(img_url):
            # 当len(img_url)等于0的时候, 就是False, not False就是True
            # 也可以理解为: img_url没有长度是执行
            # 这个判断也可以写成len(img_url==0)
                print('章节',chapter_name,'已经内容没有了')
                break
            if not os.path.exists(chapter_name):
                os.mkdir(chapter_name)
            if requests.get(img_url).status_code == 200:
                with open(os.path.join(chapter_name, img_name),'wb') as imgf:
                    imgf.write(requests.get(img_url).content)
            else:
                print('图片加载失败,没有下载图片',img_name)
        else:
            print(chapter_name + '已经内容没有了, 退出')
            break
            sleep(random.randint(3, 6))
            # 需要休眠时间,随机休眠3到5秒,这样看起来就有点类似人类的浏览
            page_num = page_num+1

if __name__ =='__main__':
    # url = 'http://www.tuku.cc/comic/28/' # 名侦探柯南
    url = 'http://www.tuku.cc/comic/17532/' # 龙珠超
    chapter_list = get_chapterlist(url)
    print(chapter_list)
    for chapter in chapter_list:
    # 遍历取出章节名,网址,依次打开页面,获取图片的网站,下载保留图片
        print(chapter_list[chapter])
        get_chapterdetail(chapter,chapter_list[chapter])
