import requests
import os

url = 'https://uncia.cc.ncu.edu.tw/dormnet/index.php?section=netflow'
d = {'ip': 'input your ip'}
r = requests.post(url, data=d)
myStart = 0
count = 0
while (True):
    pos = r.text.find("GB", myStart)
    if(myStart==0):
        pos2 = r.text.find("(", pos-10)
    else:
        pos2 = r.text.find("(", myStart)
    if (pos == -1):
        break

    myStart = pos+1
    count = count+1
    if(count==1):
        print("上傳 (校外): " + r.text[pos2+1:pos+2])
    if(count==2):
        print("下載 (校外): " + r.text[pos2+1:pos+2])
    if(count==3):
        print("上傳 (全部): " + r.text[pos2+1:pos+2])
    if(count==4):
        print("下載 (全部): " + r.text[pos2+1:pos+2])
        break
    
os.system("pause")
