from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from openpyxl import load_workbook
import xlwings as xw
import pandas as pd
import requests
import openpyxl
import time
import os

download_path = os.getcwd() + "\\downloads"
if(os.path.exists("downloads")):
    os.system(f"rmdir /Q /S downloads")
os.mkdir("downloads")
options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--mute-audio")
options.add_argument("--start-maximized")
# options.add_argument("--headless")
prefs = {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
}
options.add_experimental_option("prefs", prefs)
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service, options=options)

MAIN_URL = "https://codeforces.com"
driver.get(MAIN_URL)
time.sleep(1)
driver.find_element(By.XPATH, "//div[@class=\"roundbox menu-box borderTopRound borderBottomRound\"]//a[@href=\"/ratings\"]").click()
time.sleep(1)
users = driver.find_elements(By.XPATH, "//div[@class=\"datatable ratingsDatatable\"]//table/tbody/tr//a")
usernames = [user.text for user in users]
PROFILE_URL = "https://codeforces.com/profile/"
data = list()
profile_photos = list()
for i, username in enumerate(usernames[:50]):
    print(f"-------------------------------\n{i}")
    url = PROFILE_URL + username
    try:
        driver.get(url)
        time.sleep(0.5)
        try:
            info = driver.find_element(By.XPATH, "//div[@class=\"userbox\"]//div[@class=\"main-info \"]")
            add_info = driver.find_element(By.XPATH, "//div[@class=\"userbox\"]//div[@class=\"main-info \"]/div[2]")
        except:
            info = driver.find_element(By.XPATH, "//div[@class=\"userbox\"]//div[@class=\"main-info main-info-has-badge\"]")
            add_info = driver.find_element(By.XPATH, "//div[@class=\"userbox\"]//div[@class=\"main-info main-info-has-badge\"]/div[2]")
        rank = info.find_element(By.XPATH, "//div[@class=\"user-rank\"]")
        rating = driver.find_element(By.XPATH, "//div[@class=\"userbox\"]//div[@class=\"info\"]/ul/li[1]/span")
        profile_photo = driver.find_element(By.XPATH, "//div[@class=\"userbox\"]//div[@class=\"title-photo\"]//img").get_attribute("src")
        profile_photos.append(profile_photo)
        data.append([username, rank.text, rating.text, "img", add_info.text])
        print(f"Rank: {rank.text}\nUsername:{username}\nRating:{rating.text}\nProfile photo:{profile_photo}\nAdditional info:\n{add_info.text}")
    except Exception as e:
        print(f"Error: {e}")
        print(f"with url:{url}")
data_frame = pd.DataFrame(data, columns=["User", "Rank", "Rating", "Photo", "Additional info"])
data_frame.to_excel("codeforces.xlsx", index=False)
wb = xw.Book("codeforces.xlsx")
ws = wb.sheets["Sheet1"]
for i, photo in enumerate(profile_photos):
    img = requests.get(photo)
    with open(f"downloads\\{i}.png", "wb") as file:
        file.write(img.content)
    ws.range(f"D{i+2}").value = f'@IMAGEN("{photo}")'
    wb.app.calculate()
wb.save("codeforces.xlsx")
wb.app.quit()