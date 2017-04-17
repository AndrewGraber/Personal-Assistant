import threading
import time
import Miscellaneous

class ConnectionChecker(threading.Thread):
    def __init__(self):
        self.isConnected = Miscellaneous.checkInetConnection()
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        while True:
            if(not self.isConnected):
                self.isConnected = Miscellaneous.checkInetConnection()
                if self.isConnected: print('Connection Established... Using Wit.ai for better speech recognition')

            time.sleep(20)