import requests
from bs4 import BeautifulSoup
from secrets import username, password
import re

class FaceBookBot():
    login_basic_url = 'https://mbasic.facebook.com/login'
    login_mobile_url = 'https://m.facebook.com/login'
    payload = {
        'email': username,
        'pass': password
    }
    # post_ID = "usaplumbingheating"
    with requests.Session() as session:
        post = session.post(login_basic_url, data=payload)
        page = session.get('https://m.facebook.com/usaplumbingheating/')

    soup = BeautifulSoup(page.content, "html.parser")
    names= soup.find_all("div", {"class": "#u_0_3_w2"})
    print('names', names)
    for name in names:
        print('names', name)

    #
    # def post_content(self,request_url):
    #     with requests.Session() as session:
    #         post = session.post(self.login_basic_url, data=self.payload)
    #
    #     url = 'https://www.facebook.com/usaplumbingheating/about'
    #     print(url)
    #     r = requests.get(url)
    #     reg = r"[A-Za-z0-9.]+@[A-Za-z.]+"
    #
    #     for fb_mail in re.findall(reg, r.text):
    #         print('mail', fb_mail)
    #
    #     soup = requests.get(url).text
    #     my_html = BeautifulSoup(soup, 'lxml')
    #     list_of_likes = my_html.find_all("div", {"class": "_a58"})
    #     print(list_of_likes)
    #     # soup = BeautifulSoup(self.parse_html(REQUEST_URL).content, "html.parser")
    #     # content = soup.find_all('p')
    #     # post_content = []
    #     # for lines in content:
    #     #     post_content.append(lines.text)
    #     #
    #     # post_content = ' '.join(post_content)
    #     return self.post_content
    #
    # # def date_posted(self):
    # #     REQUEST_URL = f'https://mbasic.facebook.com/story.php?story_fbid={self.post_ID}&id=415518858611168'
    # #
    # #     soup = BeautifulSoup(self.parse_html(REQUEST_URL).content, "html.parser")
    # #     date_posted = soup.find('abbr')
    # #     return date_posted.text
    # #
    # # def post_likes(self):
    # #     limit = 200
    # #     REQUEST_URL = f'https://mbasic.facebook.com/ufi/reaction/profile/browser/fetch/?limit={limit}&total_count=17&ft_ent_identifier={self.post_ID}'
    # #
    # #     soup = BeautifulSoup(self.parse_html(REQUEST_URL).content, "html.parser")
    # #     names = soup.find_all('h3')
    # #     people_who_liked = []
    # #     for name in names:
    # #         people_who_liked.append(name.text)
    # #     people_who_liked = [i for i in people_who_liked if i]
    # #     return people_who_liked
    # #
    # # def post_shares(self):
    # #     REQUEST_URL = f'https://m.facebook.com/browse/shares?id={self.post_ID}'
    # #
    # #     with requests.Session() as session:
    # #         post = session.post(self.login_mobile_url, data=self.payload)
    # #         parsed_html = session.get(REQUEST_URL)
    # #
    # #     soup = BeautifulSoup(parsed_html.content, "html.parser")
    # #     names = soup.find_all('span')
    # #     people_who_shared = []
    # #     for name in names:
    # #         people_who_shared.append(name.text)
    # #     return people_who_shared
