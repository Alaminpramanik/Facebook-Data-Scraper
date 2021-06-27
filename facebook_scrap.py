from facebook_scraper import get_posts
from facebook_scraper import get_profile
get_profile("zuck")
for post in get_posts('nintendo', pages=1):
    print(post['text'][:50])
