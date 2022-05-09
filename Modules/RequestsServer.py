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
                db = "UTE"
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