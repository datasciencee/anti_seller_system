# 项目名称      mysite_login/core.py
# from django.conf import settings
# settings.configure()

# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite_login.settings")
import time
import requests
from lxml import etree
from . import models, views



def task():
    url = 'https://www.amazon.com/gp/offer-listing/{0}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
        'cookie': 'session - id = 137 - 9602752 - 1350111;\
                    session - id - time = 2082787201l;\
                    i18n - prefs = USD;\
                    lc - main = zh_CN;\
                    sp - cdn = "L5Z9:CN";\
                    ubid - main = 132 - 1051195 - 7521807;\
                    x - wl - uid = 1CWJV6fsO2SjJChBcKKcm5xl4NkyBSnCiyDHEpzz2BZ4WUUMOlxptW9Iy7ScG7duTmEKKrG7xScA =;\
                    session - token = IlDc / dQ4qqPTCiRCsDQFf0tT8zH + '
                                    'krqWVOcXwIQzSMCMFXl9b4Alcq9VyKNEYzUy9LDdzQLIm / gYqciFByL + '
                                    'xXopxX2k3QAWVY0XsoNszfGO8royosreZd3EAmqLCNaFLdrHBGft4E24fQHCo0Hy5b7cnLNYKSz'
                  '                 e1GFoIRfgjzXVEX24DEvGG7ZZSYDPvm7K;\
                    skin = noskin;\
                    csm - hit = tb:s - XHMQWY8QZWYQJ9X134PB | 1570501389800 & t: 1570501390113 & adb:adblk_no',
    }

    # 这个到时候的做一个循环，从数据库中取goods_id，并保存到一个列表里面
    goods_id1 = models.ConventionalInformation.objects.all()
    for i in goods_id1:
        goods_id = str(i)
        url = (url.format(goods_id))
        print(url)
        content = requests.get(url=url, headers=headers)
        tree = etree.HTML(content.text)
        # 获取店铺的url
        time.sleep(2)
        merchant_url = tree.xpath('//div[@class="a-column a-span2 olpSellerColumn"]/'
                                  'h3[@class="a-spacing-none olpSellerName"]/'
                                  'span[@class="a-size-medium a-text-bold"]/a/@href')
        print('有{0}家商店在跟卖该商品'.format(len(merchant_url)))
        if len(merchant_url) >= 1:
            print("您的商品被跟卖了")
            c = views.check_mail(requests)
            print(c)
        else:
            print("您的商品没有被跟卖")

# a = task()
#
# print(a)
