from atproto import Client
import time

from httpcore import NetworkError

client = Client()

# Using Bluesky instead of Twitter API
login = client.login('yourhandle.bsky.social','NoyMyRealPassword')
print(login.handle,login.display_name,login.followers_count)

post = client.send_post('Testing my Python script. Hey there, fellow Final Fantasy nerds!')


#2) Feed:
try:
    data = client.get_timeline(limit=30)
    feed = data.feed
    next_page = data.cursor
    for item in feed:
        print (item.post)
except NetworkError as error:
    print(f"something went wrong:{error} ")

#3) Generous Bot
def limit_handler(follower_bundle):
    try:
        while True and len(follower_bundle.followers) > 0:
            yield follower_bundle.followers.pop()
    except NetworkError as error:
        time.sleep(1000)

followers = client.get_followers(login.did)
for follower in limit_handler(followers):
    print(f"follower: {follower}")
    if follower.display_name == "whomever":
        client.follow(follower.did)

#4 Like Bot
search_string= 'Final Fantasy'
numberOfPosts = 2
count = 0
try:
    for item in feed:
       if item.post.record.text.find(search_string) > -1:
           count += 1
           client.like(item.post.uri,item.post.cid)
           if count >= numberOfPosts:
               break
except NetworkError as e:
    print(e.response)
except StopIteration as e:
    print(e)