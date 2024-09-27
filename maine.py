import instaloader
import getpass
from instaloader import Instaloader,ConnectionException

#logging in

L = instaloader.Instaloader()

username = input("Enter username: ")
password = getpass.getpass("Enter password: ")


try:
    L.login(username, password)
    print(f"Logged in successfully as {username}")


except instaloader.exceptions.BadCredentialsException:
    print("Login failed: Invalid credentials")
except instaloader.exceptions.ConnectionException as conn_error:
    print(f"Login failed: {str(conn_error)}")


#login is working now
#will start on scraping


#scraping

#initial = Instaloader(download_pictures=False, download_videos=False, download_video_thumbnails=False, save_metadata=False, max_connection_attempts=1)

#initial.load_session_from_file('gtown_datascraper1')

#def scrape(url):
    #shortcode = str(url[28:39])



