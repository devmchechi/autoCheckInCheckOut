import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

user_data_dir = r"C:\Users\{user_name}\AppData\Local\Google\Chrome\User Data" #Check Your Google User Data Path
profile_name = "Default"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--user-data-dir={user_data_dir}") 
chrome_options.add_argument(f"--profile-directory={profile_name}") 
chrome_options.add_argument("--no-sandbox") 
chrome_options.add_argument("--disable-dev-shm-usage")  
chrome_options.add_argument("--disable-gpu")  
chrome_options.add_argument("--remote-debugging-port=9222")  

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

link = "{user_link}"
def pressButton(path):
    try:
        button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(path))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(path))
        driver.execute_script("arguments[0].click();", button)
        print("Pressed Button")
    except Exception as e:
        print("Button not found", e)


clockInTime = "{clockIn_time}" # In 24 Hour %H:%M Format
clockOutTime = "{clockOut_time}" # In 24 Hour %H:%M Format

def waitTill(userTime):
    currentTime = datetime.datetime.now().strftime("%H:%M")

    while (currentTime != userTime): 
        print(f"Current time: {currentTime}. Waiting for {userTime}...")
        time.sleep(10)
        currentTime = datetime.datetime.now().strftime("%H:%M")
    print(f"Target time {userTime} reached! Proceeding to press the button...")
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(link)

def inOrOut(checkInOrOut: bool):
    if checkInOrOut:
        waitTill(clockInTime)
        pressButton((By.XPATH, "//button[contains(@aria-label, 'Check In')]"))
        print("Pressed Clock In")
    else:
        waitTill(clockOutTime)
        pressButton((By.XPATH, "//button[contains(@aria-label, 'Check Out')]"))
        print("Pressed Clock Out")

        pressButton((By.XPATH, "//label[text()='Out']"))
        print("Pressed Out")
    
    pressButton((By.XPATH, "//button[@title='OK']"))
    print("Pressed Okay")

    pressButton((By.XPATH, "//button[@title='Done']"))
    print("Pressed Done")
    
try:
    inOrOut(checkInOrOut=True)
    inOrOut(checkInOrOut=False)

except Exception as e:
    print("Something went wrong", e)
