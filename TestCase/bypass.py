# pip3 install seleniumbase
from seleniumbase import Driver

# initialize the driver in GUI mode with UC enabled
driver = Driver(uc=True, headless=False)

# set the target URL
url = "https://www.scrapingcourse.com/cloudflare-challenge"

# open URL with a 6-second reconnect time to bypass the initial JS challenge
driver.uc_open_with_reconnect(url, reconnect_time=6)