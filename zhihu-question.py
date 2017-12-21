#爬取知乎某个问题下所有答主的名字和链接
#爬取该问题下所有图片，保存到当前路径下的download的文件夹
#用selenium模拟人类行为，得到动态加载的内容
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from lxml import html as ht
from PIL import Image
from io import BytesIO
import math
import requests
import re
import os
import random


def save(text, filename='temp', path='download'):
    fpath = os.path.join(path, filename)
    with open(fpath, 'w') as  f:
        image = Image.open(BytesIO(text))
        image.save(fpath)
        print('output:', fpath)
global count
count = 0

def save_image(image_url):
    global count
    try:
        filename = image_url.split('zhimg.com/')[-1]
        print('try', filename, ' ',count)
        if os.path.exists(os.path.join('download',filename)):
            print(filename,'already exists')
            return
        resp = requests.get(image_url)
        page = resp.content
        save(page, filename)
        time.sleep(random.random())
    except:
        if (count > 5):
            return
        time.sleep(5*random.random())
        count = count +1
        save_image(image_url)
    count = 0

def crawl(url):
    resp = requests.get(url, headers=headers)
    page = str(resp.content)
    # print(page)
    # source = open("websource.txt",'r',encoding = 'utf-8')
    # page = str(source.readlines())
    # print(page)
    # reg = r'data-original="(.*?)"'
    # imgre = re.compile(reg, re.S)
    # imglist = imgre.findall(page)
    # print(imglist)
    # reg = r'data-original=.*?;(.*?)\\' #正则表达式
    # imgre = re.compile(reg, re.S)
    # imglist = imgre.findall(page)
    # image_urls = [img for img in imglist if 'http' in img]
    # print(image_urls)


    # print (page)
    root = html.fromstring(page)
    image_urls = root.xpath('//img[@data-original]/@data-original')
    print(image_urls)
    for image_url in image_urls:
        time.sleep(1)
        # print(image_url)
        save_image(image_url)

# save_image('https://pic1.zhimg.com/4ffd9427caeed1455bc8cb202e1e59dc_r.jpg')
# exit(0)

driver=webdriver.Chrome()                #用chrome浏览器打开
# driver.get('https://pic1.zhimg.com/v2-5e15368d59ad8f7b415d84c264d4da6c_r.jpg')
# print(driver)
# exit(0)
driver.get("http://www.zhihu.com")       #打开知乎我们要登录
# time.sleep(2)                            #让操作稍微停一下
driver.find_element_by_link_text('登录').click() #找到‘登录’按钮并点击
# time.sleep(5)
driver.find_element_by_class_name('signin-switch-password').click() #找到‘登录’按钮并点击
# time.sleep(2)
#找到输入账号的框，并自动输入账号 这里要替换为你的登录账号
driver.find_element_by_name('account').send_keys('')
# time.sleep(2)
#密码，这里要替换为你的密码
driver.find_element_by_name('password').send_keys('')
# time.sleep(2)
#输入浏览器中显示的验证码，这里如果知乎让你找烦人的倒立汉字，手动登录一下，再停止程序，退出#浏览器，然后重新启动程序，直到让你输入验证码
yanzhengma=input('验证码:')
# driver.find_element_by_name('captcha').send_keys(yanzhengma)
#找到登录按钮，并点击
driver.find_element_by_css_selector('div.button-wrapper.command > button').click()
cookie=driver.get_cookies()
# time.sleep(3)
driver.get('https://www.zhihu.com/question/27364360/')
# time.sleep(5)
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
answer_num = soup.select('h4.List-headerText > span')[0].get_text()
# print(answer_num)
answer_num = answer_num.split(' ')[0]
# print(answer_num)
# exit(0)

def execute_times(times):
    for i in range(times + 1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
execute_times(math.ceil(int(answer_num) / 20) - 1)

print(math.ceil(int(answer_num) / 20) - 1)

html=driver.page_source
soup=BeautifulSoup(html,'lxml')

authors = soup.select('a.UserLink-link')
author_data = [{'name':author.get_text(),'url':'https://www.zhihu.com' + author.get('href')} for author in authors]
print(author_data)
# print(html)
# img_urls = soup.select('div.RichContent-inner > span > figure > img')
# print(len(img_urls))
# img_urls = [img.get('data-original') for img in img_urls]
reg = r'data-original="(.*?)"'
imgre = re.compile(reg, re.S)
imglist = imgre.findall(html)
image_urls = [img for img in imglist if 'http' in img]
img_urls = sorted(image_urls)
print(image_urls)
# root = ht.fromstring(html)
# image_urls = root.xpath('//img[@data-original]/@data-original')
# print(image_urls)
for image_url in set(image_urls):
    time.sleep(random.random())
    # print(image_url)
    save_image(image_url)
# authors=soup1.select('a.author-link')
# authors_alls=[]
# authors_hrefs=[]
# for author in authors:
#     authors_alls.append(author.get_text())
#     authors_hrefs.append('http://www.zhihu.com'+author.get('href'))
# authors_intros_urls=soup1.select('span.bio')
# authors_intros=[]
# for authors_intros_url in authors_intros_urls:
#     authors_intros.append(authors_intros_url.get_text())
#
# for authors_all,authors_href,authors_intro in zip(authors_alls,authors_hrefs,authors_intros):
#     data={
#         'author':authors_all,
#         'href':authors_href,
#         'intro':authors_intro
#     }
#     print(data)