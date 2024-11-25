import instaloader
import pandas as pd
import time
def scrape_comments(L, shortcode, max_comments=100):
    
    L = instaloader.Instaloader()
    
    comments =[]

    # shortcode = post_url[28:39]#.split("/")[-1].strip()
    post = instaloader.Post.from_shortcode(L.context, shortcode)

    for comment in post.get_comments():
        comments.append(comment.text)
        if(len(comments)>=max_comments):
            break
        time.sleep(2)

    p = pd.DataFrame(comments, columns=["comment"])
    p.to_csv("data/unlabeled.csv", index=False)
    print(f"Scraped {len(comments)} comments")