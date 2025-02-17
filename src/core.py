from PySide6 import QtCore
import threading
import logging
import time

logger = logging.basicConfig()


class Master(QtCore.QObject):
    def __init__(self):
        self.stop = threading.Event()
        self.worker_1 = None
        self.worker_2 = None
    def init_slaves(self,worker_1,worker_2):
        self.worker_1 = worker_1
        self.worker_2 = worker_2
    def loop(self):
        print("Started Master loop")
        while not self.stop.is_set():
            time.sleep(5.0)
            self.worker_1.toggle_idle()
            self.worker_2.toggle_idle()
            with self.worker_1.idle_lock:
                print("Paused slave_1")
            with self.worker_2.idle_lock:
                print("Paused slave_2")
            self.worker_1.toggle_idle()
            self.worker_2.toggle_idle()
            print("released slaves")
        print("Finished Master loop")
        self.worker_1.stop.set()
        self.worker_2.stop.set()
        