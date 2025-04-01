# AutoCheckin & Checkout for Workday

## Description
This script automates the process of checking in and checking out from remote work on Workday. By leveraging Selenium WebDriver, it navigates to the Workday portal, logs in, and performs the required check-in and check-out actions at specified times. This ensures accurate tracking of work hours without manual intervention.

## Installation
To run this script, you need to install the required dependencies. Use the following command to install them:

```sh
pip install selenium webdriver-manager
```

## Required Files
Ensure you have the following Python modules installed:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
```

## Author
Developed by **Dev Chechi**
[LinkedIn Profile](https://www.linkedin.com/in/devmchechi)

