# test Case

# 1) Open Web Browser (Chrome/firefox/Edge).
# 2) Open URL https://opensource-demo.orangehrmlive.com/
# 3) Enter username (Admin).
# 4) Enter password (admin123).
# 5) Click on Login.
# 6) Capture title of the home page. (Actual title)
# #) Verify title of the page: OrangeHRM (Expected).
# 8) close browser

from selenium import webdriver

chromedriver_path = r'D:\NEW_W_ORDER\projects\Automation_with_python\automation_001\drivers\chromedriver-win64\chromedriver.exe'

# Create an instance of ChromeOptions
chrome_options = webdriver.ChromeOptions()

# Add any desired options to chrome_options
# For example, to run Chrome in headless mode:
chrome_options.add_argument(chromedriver_path)

# Specify the executable_path using the executable_path parameter directly
driver = webdriver.Chrome(chrome_options)








