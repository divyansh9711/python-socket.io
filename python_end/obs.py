import sys
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import parenty,socket_controller
import threading
import json
data = []
observer = None
que = None
class MyHandler(PatternMatchingEventHandler):
    patterns=["*.json"]
    global data,que
    def process(self, event):
        print("Response")
        with open('../node_message.json') as file:
            data = json.load(file)
            que.put(data)
            observer.join()
            return
    def on_modified(self, event):
        self.process(event)
        
def main():

    observer = Observer()
    observer.schedule(MyHandler(), path='../')
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

def getData():
    