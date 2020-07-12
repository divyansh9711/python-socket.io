from Naked.toolshed.shell import execute_js, muterun_js
import time  
from watchdog.observers import Observer  
from watchdog.events import PatternMatchingEventHandler  
x = "asdf"

def init():
    success = execute_js('..\\node_end\\obs.js'  + " " + x)
    return


# class MyHandler(PatternMatchingEventHandler):
#     patterns=["*.txt"]
#     def process(self, event):
#         print("asdf")
#     def on_modified(self, event):
#         self.process(event)
#     def on_created(self, event):
#         self.process(event)


# def createObserver():
#     print("createObserver")
#     observer = Observer()
#     observer.schedule(MyHandler(), path='.')
#     observer.start()

# createObserver()