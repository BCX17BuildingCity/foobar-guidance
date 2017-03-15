import json, requests

def Send(UID, data):
    payload = json.dumps({"json_payload": data})
    requests.post(UID,data=payload,headers={'content-type': 'application/json'})

def Recieve(UID):
    return requests.get(UID).json()

Send('http://100.127.9.1:3000/action','foobar')
