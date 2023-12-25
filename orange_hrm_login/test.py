# import time
#
# from selenium import webdriver
#
# from selenium.webdriver.chrome.service import Service
#
# service = Service('C:\driver\chromedriver-win64/chromedriver.exe')
#
# service.start()
#
# driver = webdriver.Remote(service.service_url)
#
# driver.get('http://www.google.com/');
#
# time.sleep(5) # Let the user actually see something!
#
# driver.quit()






import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Create ChromeOptions object
chrome_options = webdriver.ChromeOptions()

# Optional: You can add additional options here, such as headless mode
# chrome_options.add_argument('--headless')

# Set the path to chromedriver.exe
service = Service('C:\\driver\\chromedriver-win64/chromedriver.exe')

# Start the service
service.start()

# Create the webdriver instance with the ChromeOptions object
driver = webdriver.Remote(service.service_url, options=chrome_options)

# Navigate to Google
driver.get('http://www.google.com')

# Let the user see something for 5 seconds
time.sleep(5)

# Quit the driver
driver.quit()
