import requests
import json
import configparser as cfg

token = ""
chat =""

def get_token():
    parser = cfg.ConfigParser()
    parser.read("config.cfg")
    token = parser.get('creds','token')
    return token

one = "http://api.telegram.org/bot"
two = "/sendMessage?chat_id="
three = "&text="

getUpdates = "https://api.telegram.org/bot"+token+"/getUpdates"
offset = "?offset="
time = "&timeout="

# Final URL
apiUrl = one+token+two+chat+three
getUpdates = one+get_token()+"/getUpdates"

# Functions
def sendMessage(msg):
    res=''
    for e in msg.split(" "):
       res = res+'+'+e 
    requests.get(apiUrl+res)

def getdataAll():
    res = requests.get(getUpdates).text
    return json.loads(res)

def getdataId(id):
    res = requests.get(getUpdates+offset+id).text
    return json.loads(res)

def getdataPool(id,sec):
    print(token)
    res = requests.get(getUpdates+offset+id+time+sec).text
    return json.loads(res)

def sendMsg(msg,cId):
    res = requests.get(one+token+"/sendMessage?text="+msg+"&chat_id="+cId)
    print(res)

def checkMsg(msg):
    greets = ["Hi","Hello"]
    names = ["name","Name"]
    if searchStr(greets,msg):
        return "Hello! How Can i help ?"
    elif searchStr(names,msg):
        return "My name is Hyperclite bot. What is yours ?"
    else:
        return "Sorry Cant help"

def searchStr(lst,key):
    for i in lst:
        if key.find(i)!=-1:
            return 1                

## Main Code
# startId = 701287669
# for i in range(0,100):
#     startId = startId+1
#     print("running at - "+str(startId))
#     res = getdataPool(str(startId),"5")
#     if res['result']!=[]:
#         print(res['result'][0]['message']['text']+" : "+str(res['result'][0]['update_id']))
#     if res['result'][0]['message']['text']=='/send':
#         sendMessage("test")

startId = 701287715
while True:
    get_token()
    startId = startId+1
    res = getdataPool(str(startId),"50")
    print(res)
    if res['ok']==False:
        print("Error")
        print(res)
    elif res['result']!=[]:
        print(res['result'][0]['message']['text']+" : "+str(res['result'][0]['update_id']))
    sendMsg(checkMsg(res['result'][0]['message']['text']),str(res['result'][0]['message']['chat']['id']))        