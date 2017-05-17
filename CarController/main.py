import thread

from RpiCam import RpiCam
from Dispacher import Dispatcher
from DriveController import DriveController
from KeyboardListenner import KeyboardListenner

drive = DriveController()
keyboard = KeyboardListenner()

dispatcher = Dispatcher(drive)


def startInputListenner(threadName, delay):
    while 1:
        x = str(keyboard.getKey())
        #print "key: ", x
        dispatcher.dispatche(x)
try:
    thread.start_new_thread(startInputListenner, ("keyboard", 2,))
except:
    print "Error: unable to start thread"

#camera = RpiCam()
#camera.showPreview()


while 1:
    # Do another stuff
    pass
