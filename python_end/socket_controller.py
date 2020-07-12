import json
import parenty,threading,obs
from waiting import wait
data_status = False
response_data = None
data = {}
data['requestType'] = "none"
data['route'] = "message"
data['data'] = "hola amigo"
data['nameSpace'] = "localhost"
def initChild():
    parenty.init()




def init_comm_file():
    print("init me")
    x = threading.Thread(target = initChild,args = ())
    x.start()
    print('Initializing python side communication file')
    with open('../python_message.txt', 'w') as outfile:
        json.dump(data, outfile)
        return

def request_connection():
    print('Requesting connection')
    global data
    data['requestType'] = "init"
    data['namespace'] = "localhost"
    data['route'] = "message"
    with open('../python_message.txt', 'w') as file:
        json.dump(data, file)
        return

def response(response):
    global data_status,response_data
    data_status = True
    response_data = response

def request_general(requestType,dataR):
    global response_data
    print("Requesting")
    global data
    data['data'] = dataR
    data['requestType'] = requestType
    with open('../python_message.txt', 'w') as file:
        print(data)
        json.dump(data, file)
    wait(lambda: data_status)
    print(response_data)
    return