import instaloader
import pandas as pd

def scrape_comments(username, post_url, max_comments=100):
    
    L = instaloader.Instaloader()
    
    comments =[]

    shortcode = str(post_url[28:39])

    for comment in shortcode.get_comments():
        comments.append(comment.text)
        if(len(comments)>=max_comments):
            break

    p = pd.DataFrame(comments, columns=["comment"])
    p.to_csv("data/unlabeled.csv", index=False)
    print(f"Scraped {len(comments)} comments")