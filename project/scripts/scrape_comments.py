import instaloader
import pandas as pd

def scrape_comments(L, post_url, max_comments=100):
    
    L = instaloader.Instaloader()
    
    comments =[]

    shortcode = post_url.split("/")[-1].strip()
    post = instaloader.Post.from_shortcode(L.context, shortcode)

    for comment in post.get_comments():
        comments.append(comment.text)
        if(len(comments)>=max_comments):
            break

    p = pd.DataFrame(comments, columns=["comment"])
    p.to_csv("data/unlabeled.csv", index=False)
    print(f"Scraped {len(comments)} comments")