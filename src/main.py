from PySide6 import QtCore
from src.core import Master
from src.mfc import Slave
import threading
import time

if __name__ == "__main__":
    threads_ = QtCore.QThreadPool()
    idle_lock_1 = threading.Lock()
    idle_lock_2 = threading.Lock()
    slave_1 = Slave(idle_lock_1)
    slave_2 = Slave(idle_lock_2)
    master_ = Master()
    master_.init_slaves(slave_1,slave_2)
    threads_.start(master_.loop)
    threads_.start(slave_1.loop)
    threads_.start(slave_2.loop)
    time.sleep(50.0)
    master_.stop.set()
    time.sleep(10.0)