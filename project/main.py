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




