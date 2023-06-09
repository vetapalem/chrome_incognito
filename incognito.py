from selenium import webdriver as wb
from selenium.webdriver.chrome.service import Service
#main point
from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.common.options import
from webdriver_manager.chrome import ChromeDriverManager as ch
import time as tt


dri=Options()
dri.add_argument("incognito")


dir=wb.Chrome(executable_path=ch().install(),options=dri)

#youtube
dir.get(url=r'your url')
dir.maximize_window()
tt.sleep(45)
dir.quit()