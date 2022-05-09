import re


# convert accent vietnamese to no
def no_accent_vietnamese(s):
    s = s.lower()
    s = re.sub('[áàảãạăắằẳẵặâấầẩẫậ]', 'a', s)
    s = re.sub('[éèẻẽẹêếềểễệ]', 'e', s)
    s = re.sub('[óòỏõọôốồổỗộơớờởỡợ]', 'o', s)
    s = re.sub('[íìỉĩị]', 'i', s)
    s = re.sub('[úùủũụưứừửữự]', 'u', s)
    s = re.sub('[ýỳỷỹỵ]', 'y', s)
    s = re.sub('đ', 'd', s)
    return s

# remove spacial and residual character 
def special_characters(str):
    str = re.sub(r"[^a-eg-ik-vxyA-EG-IK-VXY0-9 ]","",str)
    index = 0
    for i in str:
        if index != 0:
            if 'sxr'.find(i)>=0:
                if str[index-1] != ' ':
                    str =str.replace(str[index-1]+i,str[index-1])
                    index-=1
            if i == str[index-1]:
                str = str.replace(i+i,i)
                index-=1
        index+=1
    return str

# find a like b
def like(a,b):
    a = a.split(" ")
    for i in a:
        if b.find(i) < 0:
            return False
    return True

# check list a like b 
def check(a,b):
    for i in a:
        if like(i,b):
            return True
    return False