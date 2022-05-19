from lxml import html
import requests
from bs4 import BeautifulSoup
import json
def crawl_data():
    BGH_PATH = "https://ute.udn.vn/LoaiBoPhan/1/Ban-Giam-hieu.aspx"
    sinhvienPATH = "https://sinhvien.ute.udn.vn/default.aspx#"
    # 
    result = requests.get(sinhvienPATH)
    soup = BeautifulSoup(result.content,"html")
    data = soup.find("h3",itemprop="name")
    active = ""
    for i in data:
        if i != "\n":
            if active == "":
                active+=i.text
            else:
                active+=", "+i.text
    tree = requests.get(BGH_PATH)
    soup = BeautifulSoup(tree.content,"html")
    result = soup.find_all("strong")
    strr = []
    for i in result:
        strr.append(i.text)
    for i in strr:
        i = str(i).replace('\xa0',' ')
    json_data = {
        "intents" : [{
            "tag": ["HIỆU TRƯỞNG"],
            "questions": ["Hiệu trưởng"],
            "answers" : []
        },
        {
            "tag": ["PHÓ HIỆU TRƯỞNG"],
            "questions": ["hiệu phó"],
            "answers" : []
        },
        {
            "tag": ["hoạt động"],
            "questions": ["hoạt động đang mở","hoạt động","chương trình"],
            "answers" : [active]
        }
        ]
    }
    for i in json_data["intents"]:
        count = 0
        for j in strr:
            for k in i["tag"]:
                if k == j:
                    if i["answers"] == []:
                        i["answers"].append(strr[count+1])
                    else:
                        for ii in i["answers"]:
                            ii+=", "+strr[count+1]
                            i["answers"] = [ii]
            count+=1
    f = open("data/UTE.json",'w+', encoding="utf-8")
    f.write(json.dumps(json_data))
    f.close()
