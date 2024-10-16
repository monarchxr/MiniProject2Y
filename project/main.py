import instaloader
import getpass
from instaloader import Instaloader,ConnectionException
from scripts.scrape_comments import scrape_comments

#logging in

L = instaloader.Instaloader()

username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

L.context.log("debug")
try:
    L.login(username, password)
    print(f"Logged in successfully as {username}")


except instaloader.exceptions.BadCredentialsException:
    print("Login failed: Invalid credentials")


post_url = input("Enter post url: ")
scrape_comments(L, post_url)