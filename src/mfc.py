from PySide6 import QtCore
import threading
import logging

logger = logging.basicConfig()


class Slave(QtCore.QObject):
    def __init__(self,lock):
        self.stop = threading.Event()
        self.pause_event = threading.Event()
        self.idle_lock = lock
    
    def loop(self):
        print("Started slave loop")
        while not self.stop.is_set():
            if self.pause_event.is_set():
                with self.idle_lock:
                    print("Pause slave lock")
                    self.idle_state = True
                while self.pause_event.is_set():
                    pass
                with self.idle_lock:
                    print("Release slave lock")
                    self.idle_state = False
        print("Finished slave loop")
    
    
    @QtCore.Slot()
    def toggle_idle(self):
        if self.pause_event.is_set():
            self.pause_event.clear()
        else:
            self.pause_event.set()