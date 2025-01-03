import instaloader
import getpass
from instaloader import Instaloader,ConnectionException,PostComment
from scripts.scrape_comments import scrape_comments
import pandas as pd
import time
from datetime import datetime

#logging in

L = instaloader.Instaloader()

username = input("Enter username: ")
# password = getpass.getpass("Enter password: ")

# L.context.log("debug")
try:

    L.interactive_login(username)

    print(f"Logged in successfully as {username}")


except instaloader.exceptions.BadCredentialsException:
    print("Login failed: Invalid credentials")


shortcode = input("Enter post shortcode: ")

#function to generate a unique filename

def gen_filename():
    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
    base = "unlabeled"

    filename = "_".join([base,timestamp])

    return filename

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
p['label'] = None
csv_filename = gen_filename()
p.to_csv(f"/workspaces/MiniProject2Y/project/data/{csv_filename}", index=False)
print(f"Comments saved to {csv_filename}")
print(f"Scraped {len(comments)} comments")