# My_First_Selenium_Test

To install Selenium using PyCharm, follow these step-by-step instructions:


### **Step 1: Install Selenium**
1. In the terminal, type the following command and press **Enter**:
   pip install selenium
PyCharm will download and install Selenium along with its dependencies.

### **Step 2: Install webdriver**
This command installs the webdriver-manager Python package, which is used to automatically manage browser drivers like ChromeDriver.
 pip install webdriver_manager 

Benefits of webdriver-manager
✅ No need to manually download or update drivers
✅ Works for multiple browsers (Chrome, Firefox, Edge, IE)
✅ Reduces setup time for Selenium WebDriver

### **Step 3: Test Selenium with ChromeDriver **
Create a new Python file in PyCharm and add this code:
   ```python
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
  