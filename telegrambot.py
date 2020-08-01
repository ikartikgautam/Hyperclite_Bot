import requests
import json

token = "<YOUR BOTS ID HERE>"
chat = "@testing0694"

one = "http://api.telegram.org/bot"
two = "/sendMessage?chat_id="
three = "&text="

getUpdates = "https://api.telegram.org/bot"+token+"/getUpdates"
offset = "?offset="
time = "&timeout="

# Final URL
apiUrl = one+token+two+chat+three
getUpdates = one+token+"/getUpdates"

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
    res = requests.get(getUpdates+offset+id+time+sec).text
    return json.loads(res)

## Main Code
startId = 701287669
for i in range(0,100):
    startId = startId+1
    print("running at - "+str(startId))
    res = getdataPool(str(startId),"5")
    if res['result']!=[]:
        print(res['result'][0]['message']['text']+" : "+str(res['result'][0]['update_id']))
    if res['result'][0]['message']['text']=='/send':
        sendMessage("test")