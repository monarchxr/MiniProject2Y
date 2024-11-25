import instaloader
import getpass
from instaloader import Instaloader,ConnectionException
from scripts.scrape_comments import scrape_comments
import pandas as pd
import time

#logging in

L = instaloader.Instaloader()

username = input("Enter username: ")
# password = getpass.getpass("Enter password: ")

L.context.log("debug")
try:
    # L.login(username, password)
    L.interactive_login(username)
    # L.load_session_from_file(username)
    print(f"Logged in successfully as {username}")


except instaloader.exceptions.BadCredentialsException:
    print("Login failed: Invalid credentials")


shortcode = input("Enter post shortcode: ")
# scrape_comments(L, shortcode)

comments =[]

# shortcode = post_url[28:39]#.split("/")[-1].strip()
post = instaloader.Post.from_shortcode(L.context, shortcode)
max_comments = 100
for comment in post.get_comments():
    comments.append(comment.text)
    if(len(comments)>=max_comments):
        break
    time.sleep(2)

    p = pd.DataFrame(comments, columns=["comment"])
    p.to_csv("/workspaces/MiniProject2Y/project/data/unlabeled.csv", index=False)
    print(f"Scraped {len(comments)} comments")