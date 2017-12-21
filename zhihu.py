# -*- coding: utf-8 -*-
#爬取知乎某个回答的所以图片
import os
import time
import requests
import re
from lxml import html
from PIL import Image
from io import BytesIO

headers = {
    'Host': 'www.zhihu.com',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    # 2017.12 经网友提醒，知乎更新后启用了网页压缩，所以不能再采用该压缩头部
    # !!!注意, 请求头部里使用gzip, 响应的网页内容不一定被压缩，这得看目标网站是否压缩网页
    # 'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
}


def save(text, filename='temp', path='download'):
    fpath = os.path.join(path, filename)
    with open(fpath, 'w') as  f:
        image = Image.open(BytesIO(text))
        print('output:', fpath)
        image.save(fpath)


def save_image(image_url):
    resp = requests.get(image_url)
    page = resp.content
    filename = image_url.split('zhimg.com/')[-1]
    save(page, filename)


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
    # image_urls = ['https://pic3.zhimg.com/fe7bdd75b701d74666daeda255c7abca_r.jpg', 'https://pic3.zhimg.com/fe7bdd75b701d74666daeda255c7abca_r.jpg', 'https://pic3.zhimg.com/b2ff83fa4438304267930b67b9a6189a_r.jpg', 'https://pic1.zhimg.com/a49f7d68e0e7c76f900b1556de91227c_r.jpg', 'https://pic1.zhimg.com/2b5e7f03a0f467f2eb5fb65f84a8e5c0_r.jpg', 'https://pic3.zhimg.com/79443e71708d173618ae41d9528867ba_r.jpg', 'https://pic2.zhimg.com/v2-274a6ac4764d3824987fcd99874247fd_r.jpg', 'https://pic4.zhimg.com/v2-4b3fb8aad126f9a6f3062e4715385a53_r.jpg', 'https://pic2.zhimg.com/v2-09ad68c54031551cc59763c2e657b651_r.jpg', 'https://pic4.zhimg.com/83b1048cdd7ecd03583f2476077f25c3_r.jpg', 'https://pic2.zhimg.com/eb323181ad46cc66afef9b21527096f5_r.jpg', 'https://pic3.zhimg.com/v2-a6f48368a418bb6606da9c67331a5dfa_r.jpg', 'https://pic1.zhimg.com/5ffcea923b909dc33ec63027c674cac8_r.jpg', 'https://pic1.zhimg.com/v2-05c87c278d242402a56fa628fb55efd4_r.jpg', 'https://pic1.zhimg.com/v2-05c87c278d242402a56fa628fb55efd4_r.jpg', 'https://pic4.zhimg.com/e7fee3a96558d4862175b54a600b8193_r.jpg', 'https://pic1.zhimg.com/1e04fe41fd0c7ced53b1d59c20d2c41c_r.jpg', 'https://pic2.zhimg.com/f7c3167104216a7370855e91e9bfabf5_r.jpg', 'https://pic2.zhimg.com/bd626b1dadc32c81672e6f2e94c0c56d_r.jpg', 'https://pic2.zhimg.com/0096a435a415609c22c60c7748bfd0c5_r.jpg', 'https://pic3.zhimg.com/50cd6e65fccf81638232525cafe56eae_r.jpg', 'https://pic2.zhimg.com/4bb9b4649b3431a84b87e572e5627e79_r.jpg', 'https://pic3.zhimg.com/5d570ed1b349cc75673d384bd3479db2_r.jpg', 'https://pic1.zhimg.com/6bb2751257a3abed0fcdadb8472ba030_r.jpg', 'https://pic2.zhimg.com/556a6af78b22f337c7affa57c6a26a19_r.jpg', 'https://pic2.zhimg.com/ec51141db2f9d5d0b9c7679ab3e5c901_r.jpg', 'https://pic2.zhimg.com/18e182df077c3e14a3b93be3bb70378d_r.jpg', 'https://pic2.zhimg.com/7e7c29cb4e501cef3f321ebbc08faf19_r.jpg', 'https://pic2.zhimg.com/62508508a40d1019ab010009d288c3d9_r.jpg', 'https://pic3.zhimg.com/905ad171a0eaa5c9ab07d50c5c586db6_r.jpg', 'https://pic1.zhimg.com/6e1f2ecfe692b41071453f1415b6a8d8_r.jpg', 'https://pic4.zhimg.com/1617b419a086c249b159b51db79d9c1b_r.jpg', 'https://pic4.zhimg.com/d29eef454a9e721e0a5ec008e5618ae3_r.jpg', 'https://pic2.zhimg.com/cd64552122897252d8afdb5864ff8dc1_r.jpg', 'https://pic2.zhimg.com/e248043b46492f95a8e3451d802f2d8d_r.jpg', 'https://pic1.zhimg.com/4ffd9427caeed1455bc8cb202e1e59dc_r.jpg', 'https://pic2.zhimg.com/74d224d21c55bd714a8e693290aa770d_r.jpg', 'https://pic3.zhimg.com/dce8578214f6714f3ef32c7455dd94f2_r.jpg', 'https://pic2.zhimg.com/67e123d90b1756620a4a89f7fa4d7611_r.jpg', 'https://pic3.zhimg.com/d8cefb92dd2f96e358cdfe0140d6cef2_r.jpg', 'https://pic2.zhimg.com/39d8a8290e4d397350899543f5857a59_r.jpg', 'https://pic1.zhimg.com/66a6d71333169d8d226c5e279457355c_r.jpg', 'https://pic1.zhimg.com/9319a31a300a3c12d6022ede1964a99c_r.jpg', 'https://pic1.zhimg.com/aef0a40f9469d66ce7af7be9b3e53008_r.jpg', 'https://pic3.zhimg.com/34a00bea282d5b2dd175428a78e07c52_r.jpg', 'https://pic2.zhimg.com/8df6a7cf3fc4695e45a9ccdd5b0d8735_r.jpg', 'https://pic4.zhimg.com/3c1664e0fb49684b04fbd29193d19423_r.jpg', 'https://pic2.zhimg.com/a54811525fe924cb588a9d60a0615a71_r.jpg', 'https://pic4.zhimg.com/022fd4723405a06435889b08964c142f_r.jpg', 'https://pic2.zhimg.com/cf47af4b8b83ebc9bd9f21f7b5e2a9b9_r.jpg', 'https://pic2.zhimg.com/19500447a75df0292ea3d7202e03b391_r.jpg', 'https://pic2.zhimg.com/0eb94238af6cc2ead7ec48dae3ee70c9_r.jpg', 'https://pic1.zhimg.com/fea6b4b414e1bfa52660d8d251626524_r.jpg', 'https://pic2.zhimg.com/990745d097f3a28aeab16bbe930c4475_r.jpg', 'https://pic1.zhimg.com/a26de02a3834965f9aeeb5dc8f2a0254_r.jpg', 'https://pic1.zhimg.com/a26de02a3834965f9aeeb5dc8f2a0254_r.jpg', 'https://pic1.zhimg.com/416ce818ce3c6010f6035c86278d7974_r.jpg', 'https://pic1.zhimg.com/416ce818ce3c6010f6035c86278d7974_r.jpg', 'https://pic2.zhimg.com/b4d681d3fc9c430a230de41ac0a2dcdd_r.jpg', 'https://pic3.zhimg.com/126abc3790bb5622169d23cd3deb68b2_r.jpg', 'https://pic4.zhimg.com/4aabb6e7b0beec2b14f6826f178371d7_r.jpg', 'https://pic4.zhimg.com/6ca6a6626240876d5301f17994c7f153_r.jpg', 'https://pic4.zhimg.com/114160a7f6beb3e5d87aa37d0637d163_r.jpg', 'https://pic2.zhimg.com/b094c1ff80243a75709ab488077253c5_r.jpg', 'https://pic4.zhimg.com/8463c683d76d5abe4385d336e814f5b3_r.jpg', 'https://pic3.zhimg.com/cccbf98f592ad5cb0f5337fac5badf5e_r.jpg', 'https://pic3.zhimg.com/71cb6509bb04bf6b0fad69acd44f50d2_r.jpg', 'https://pic3.zhimg.com/71cb6509bb04bf6b0fad69acd44f50d2_r.jpg', 'https://pic2.zhimg.com/84103816d7d3ba2b7619ca59b8ab77dd_r.jpg', 'https://pic2.zhimg.com/27aaf422b516689a06c34eeb7bc3c97d_r.jpg', 'https://pic3.zhimg.com/b468123ff7098aebdf29f443064519b2_r.jpg', 'https://pic2.zhimg.com/0a0f8f0392f2987fd7dbc07db4ea5da5_r.jpg', 'https://pic4.zhimg.com/51d63b958f7b4a1ae8bab9dc4d62789f_r.jpg', 'https://pic3.zhimg.com/af26da2191a8fcb894597ae8200b0b12_r.jpg', 'https://pic1.zhimg.com/5b28a22060ad0f42105bc38129e2318c_r.jpg', 'https://pic3.zhimg.com/19586df7f9edea0775a93c09e83e514a_r.jpg', 'https://pic2.zhimg.com/70b90a836d94c9bb566c9bc6024b9135_r.jpg', 'https://pic3.zhimg.com/488ae68b766e30ad6555a69207f81e7a_r.jpg', 'https://pic3.zhimg.com/996edbbb5a6acc82620b9add19d2857a_r.jpg', 'https://pic1.zhimg.com/75ba8c18f3a073d7313598c9d512ce84_r.jpg', 'https://pic4.zhimg.com/057ba272fde629895f988eeca10e1bc3_r.jpg', 'https://pic4.zhimg.com/057ba272fde629895f988eeca10e1bc3_r.jpg']
    for image_url in image_urls:
        time.sleep(1)
        # print(image_url)
        save_image(image_url)


if __name__ == '__main__':
    # 注意在运行之前，先确保该文件的同路径下存在一个download的文件夹, 用于存放爬虫下载的图片
    url = 'https://www.zhihu.com/question/27364360/answer/36350520'  # 有一双美腿是一种怎样的体验?
    crawl(url)


