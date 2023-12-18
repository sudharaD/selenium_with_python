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

# Specify the path to the chromedriver executable
chromedriver_path = r'D:\NEW_W_ORDER\projects\Automation_with_python\automation_001\drivers\chromedriver-win64\chromedriver.exe'

# Create ChromeOptions instance
chrome_options = webdriver.ChromeOptions()

# Set any desired options here, if needed
# chrome_options.add_argument('--headless')

# Specify the path to the chromedriver executable directly in the options
chrome_options.binary_location = chromedriver_path

# Create the WebDriver instance with the specified options
driver = webdriver.Chrome(chrome_options)


driver.get('https://opensource-demo.orangehrmlive.com/')