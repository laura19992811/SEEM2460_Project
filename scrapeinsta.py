from instascrape import Location

url = 'https://www.instagram.com/explore/locations/214424288/hong-kong/'
hk = Location(url)
hk.scrape()
recent_posts = hk.get_recent_posts()
for posts in recent_posts:
    posts.to_csv("posts.txt")