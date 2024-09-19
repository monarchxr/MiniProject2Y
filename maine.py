import instaloader
from instaloader import Instaloader,ConnectionException

#logging in

L = instaloader.Instaloader

username = input("Enter username: ")

L.interactive_login(username)
L.load_session_from_file(username)

instaloader = Instaloader(max_connection_attempts=1)

try:
    username = instaloader.test_login()
    if not username:
        raise ConnectionException()
except ConnectionException:
    raise SystemExit("Are you logged in?")

instaloader.save_session_to_file()

#not sure if login works, ill test 


#scraping

initial = Instaloader(download_pictures=False, download_videos=False, download_video_thumbnails=False, save_metadata=False, max_connection_attempts=1)

initial.load_session_from_file('gtown_datascraper1')

def scrape(url):
    shortcode = str(url[28:39])



