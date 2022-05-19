import json
from datetime import date, datetime
import random
from Modules import HandleString as hs

#main requests
def main_requests(userText, db):
    hour = ["mấy giờ","giờ hiện tại","bây giờ mấy giờ"]
    day = ["hôm nay ngày","ngày hiện tại","hôm ni ngày"]
    if hs.check(hour,userText):
        return datetime.now().strftime("%H:%M:%S")
    else:
        if hs.check(day,userText):
            return datetime.now().strftime("%d/%m/%Y")
        else:
            if db == "":
                db = "InforGroup"
            return getRespone(userText,db)

# get response 
def getRespone(userText,db):
    with open("data/"+db+".json",encoding='utf-8') as file:
        data = json.load(file)
    for intents in data["intents"]:
        for tag in intents["tag"]:
            if hs.like(hs.special_characters(hs.no_accent_vietnamese(str(tag))),hs.special_characters(hs.no_accent_vietnamese(str(userText)))):
                for questions in intents['questions']:
                    if hs.special_characters(hs.no_accent_vietnamese(userText)).find(hs.special_characters(hs.no_accent_vietnamese(questions))) >=0:
                        return intents["answers"][random.randint(0, len(intents["answers"])-1)]
    for intents in data["intents"]:
        for questions in intents['questions']:
            if hs.special_characters(hs.no_accent_vietnamese(userText)).find(hs.special_characters(hs.no_accent_vietnamese(questions))) >=0:
                return intents["answers"][random.randint(0, len(intents["answers"])-1)]
    return "Thông tin này AI chưa được học :D"

def getLichThi(user , password):
    chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path
    chrome_options = webdriver.ChromeOptions()
# setting headless parameter
    chrome_options.headless = True
    driver = webdriver.Chrome()
    driver.get("http://daotao.ute.udn.vn/viewsmsg.asp")
    driver.find_element_by_name("maSV").send_keys(user)
# find password input field and insert password as well
    driver.find_element_by_name("pw").send_keys(password)
# click login button
    driver.find_element_by_xpath("//tbody//tr//td//input[@type='submit']").click()
    dataa = []
    driver.get("http://daotao.ute.udn.vn/dkmhtc.asp")
    dataa = driver.find_element_by_xpath("//div[@class='clearfix']//div//table//tbody//tr//div//li").text
    return dataa