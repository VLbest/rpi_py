from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import thread
import matplotlib.pyplot as plt


class RpiCam(object):
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (640, 432)
        self.camera.framerate = 24
        self.rawCapture = PiRGBArray(self.camera, size=(640, 432))

    def showPreview(self):
        try:
            thread.start_new_thread(self.startCameraThread, ("camera", 2))
        except:
            print "Error: unable to start camera thread"

    def startCameraThread(self, threadName, delay):
        for frame in self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
            image = frame.array
            cv2.imshow("Frame", image)
            key = cv2.waitKey(1)
            self.rawCapture.truncate(0)
