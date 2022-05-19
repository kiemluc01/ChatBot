import json
from datetime import date, datetime
import random
from Modules import HandleString as hs
import chromedriver_autoinstaller
from selenium import webdriver
import numpy as np
import pandas as pd

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
    chrome_options = webdriver.ChromeOptions()
    # setting headless parameter
    chrome_options.headless = True
    driver = webdriver.Chrome(chrome_options =chrome_options)
    driver.get("http://daotao.ute.udn.vn/viewsmsg.asp")
    # username = "1911505310246"
    # password = "190201"
    driver.find_element_by_name("maSV").send_keys(user)
    # find password input field and insert password as well
    driver.find_element_by_name("pw").send_keys(password)
    # click login button

    driver.find_element_by_xpath("//tbody//tr//td//input[@type='submit']").click()

    if(user.isnumeric()):
        dataa = []
        dataaa = []
        dataaa = driver.find_element_by_xpath("//td[@id='pagemain']").text
        if(str(dataaa).find("Đăng nhập không hợp lệ") >= 0):
            print("Tài khoản hoặc mật khẩu không chính xác!!!")
        else:
            driver.get("http://daotao.ute.udn.vn/dkmhtc.asp")
            dataa = driver.find_element_by_xpath("//div[@class='clearfix']//div//table//tbody//tr//div//li")
            print(dataa.text)
    else:
        print("tài khoản hoặc mật khẩu không chính xác!!!")
def lichhoc(maSV):
    chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

    chrome_options = webdriver.ChromeOptions()
# setting headless parameter
    chrome_options.headless = True
    driver = webdriver.Chrome(chrome_options = chrome_options)
    driver.get("http://daotao.ute.udn.vn/timetable.asp")
    driver.find_element_by_name("maSV").send_keys(maSV)
    if(maSV.isnumeric()):
        driver.find_element_by_xpath("//form[@action='svtkb.asp']//table//tbody//tr//td//table//tbody//tr//td//input[@type='submit']").click()
        data =[]
        data = driver.find_elements_by_xpath("//table[@bgcolor='#E7EBDE']//tbody//tr")
# result = requests.get(driver)
# soup = BeautifulSoup(driver,"html.parser")
# result = str(data).split(" ")
        d =0
        head = data[0]
        for i in data:
            if d!= 0 and i.text.find("Lớp")>=0:
                d-=1
                break
            d+=1
        result = []
        data = driver.find_elements_by_xpath("//table[@bgcolor='#E7EBDE']//tbody//tr//th")
        for i in range(9):
            result.append([])

        data = driver.find_elements_by_xpath("//table[@bgcolor='#E7EBDE']//tbody//tr//td")
        for i in range(d*9):
            result[i%9].append(str(data[i].text))
        dt = pd.DataFrame(np.array(result))
        print(display(dt))
        return dt
    return "Mã sinh viên không đúng"
def hocphi():
    driver.get("http://daotao.ute.udn.vn/viewmsg.asp")
    a = driver.find_elements_by_xpath("//td[@id='pagemain']//a")
    # a = driver.find_elements_by_xpath("//td[@id='pagemain']//table//tbody//tr//td//a")
    for i in a:
    #     print(i.text)
        if i.text.find("thu học phí")>=0:
            i.click()
            break
    td = driver.find_element_by_xpath("//td[@style='font-size:14px;padding-left: 1em']").text
    print(str(td).split("\n")[0])
    strr = str(td).split("\n")[0]
    index = strr.find("ngày")
    print(strr[index:len(strr)])
    data = strr[index:len(strr)]
    return data