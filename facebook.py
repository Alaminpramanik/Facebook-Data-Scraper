import random

from bs4 import BeautifulSoup
import requests
import re
from proxy import *
PROXIES_LIST_ = []
url = 'https://www.facebook.com/newyorkplumbing/'
response = requests.get(url)
soup = BeautifulSoup(response.content,'lxml')
f = soup.find('div', attrs={'class': '._2pi2+ ._2pi2 ._4bl9 > div'})
likes=soup.find('span',attrs={'class':'_4bl9'})

#finding span tag inside class
print(likes.text)


#
# def make_soup(url, retry):
#     global proxy_string
#     for row in proxy_string.split():
#         if row:
#             PROXIES_LIST_.append(row.strip())
#             pass
#
#     print(PROXIES_LIST_)
#
#     proxyDict = {
#               "http"  : random.choice(PROXIES_LIST_),
#               "https" : random.choice(PROXIES_LIST_),
#               "ftp"   : random.choice(PROXIES_LIST_)
#             }
#     try:
#         html = requests.get(url, headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}, proxies=proxyDict).content
#     except:
#         print("Fail to request " + url + " with proxy: " + str(proxyDict['https']))
#         if retry < 0:
#             return None
#         else:
#             return make_soup(url, retry-1)
#     return BeautifulSoup(html,'lxml')
# # user = 'usaplumbingheating'
#
# def facebook():
#     pass


#
# def facebook():
#     website = f"https://www.facebook.com/usaplumbingheating/about"
#     print('website', website)
#     r = requests.get(website)
#     reg = r"[A-Za-z0-9.]+@[A-Za-z.]+"
#     for fb_mail in re.findall(reg, r.text):
#         print('mail', fb_mail)
#     soup = requests.get(website).text
#     my_html = BeautifulSoup(soup, 'lxml')
#
#     list_of_likes = my_html.find_all('span', class_='d2edcug0')
#     print(list_of_likes)
#
#     for i in list_of_likes:
#         print(i)
#
#     return facebook()
