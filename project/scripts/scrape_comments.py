import instaloader
import pandas as pd
import time

def scrape_comments(session_username, post_url_shortcode, output_file, max_comments=100):
    
    L = instaloader.Instaloader()

    try:
        L.load_session_from_file(session_username)  
        print("Session loaded successfully!")
    except FileNotFoundError:
        print(f"Session file not found for user '{session_username}'")
        return
    except Exception as e:
        print(f"Error loading session: {e}")
        return

    comments = []
    try:
        print(post_url_shortcode) 
        post = instaloader.Post.from_shortcode(L.context, post_url_shortcode)
        print(f"Fetching comments for post: {post_url_shortcode}")

        for comment in post.get_comments():
            comments.append(comment.text)
            print("Scraped", len(comments), "comments")
            if len(comments) >= max_comments:
                break
            time.sleep(2)

    except Exception as e:
        print(f"Error fetching post/comments: {e}")
        return

    try:
        df = pd.DataFrame(comments, columns=["comment"])
        df.to_csv(output_file,mode='w',header=False ,index=False)
        print(f"Scraped {len(comments)} comments and saved to {output_file}")
    except Exception as e:
        print(f"Error saving comments: {e}")

if __name__ == "__main__":
    session_username = "_monarchxr_"
    post_url_shortcode = input("Enter Instagram post URL shortcode: ")
    output_file = r"C:\Users\rauna\OneDrive\Desktop\MiniProject2Y\project\data\unlabeled.csv" 
    scrape_comments(session_username, post_url_shortcode, output_file)