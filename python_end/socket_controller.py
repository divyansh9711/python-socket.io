import json
import parenty,threading,obs,queue
responseData = False
data = {}
data['requestType'] = "none"
data['route'] = "message"
data['data'] = "hola amigo"
data['nameSpace'] = "localhost"
def initChild():
    parenty.init()

def callObs(q):
    obs.main(q)


def init_comm_file():
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

def response(data):
    print(data)

def request_general(requestType,dataR):
    print("Requesting")
    que = queue.Queue()
    global data
    data['data'] = dataR
    data['requestType'] = requestType
    with open('../python_message.txt', 'w') as file:
        print(data)
        json.dump(data, file)

    t = threading.Thread(target = callObs, args=(que,))
    t.start()
    t.join()
    print(que)
    return