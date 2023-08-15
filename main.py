from selenium import webdriver

PATH = "C:\Program Files (x86)\Code\chrome-win64\chrome.exe"
chrome_options = webdriver.ChromeOptions()
chrome_service = webdriver.ChromeService(PATH)
driver = webdriver.Chrome(options=chrome_options, service=chrome_service)

driver.get('https://youtube.com/')
# driver.switch_to.new_window('window')