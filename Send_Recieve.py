def Send(UID, data):
    import json, requests
    request.get(UID,data=json.dump(data))

def Recieve(UID):
    import json, requests
    return request.get(UID).json()
