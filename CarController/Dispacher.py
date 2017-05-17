class Dispatcher(object):


    def __init__(self, drive):
        self.driveController = drive

    def dispatche(self, key):
        key = str(key)[0]
        if key == 'z':
            self.driveController.goForward()
        elif key == "s":
            self.driveController.goBackward()
        elif key == "x":
            self.driveController.TurnOffEverything()
        elif key == "0":
            self.driveController.SetSpeedVerySlow()
        elif key == "2":
            self.driveController.SetSpeedSlow()
        elif key == "5":
            self.driveController.SetSpeedNormal()
        elif key == "8":
            self.driveController.SetSpeedMax()
        elif key == "d":
            self.driveController.TurnToLeft()
        elif key == "q":
            self.driveController.TurnToRight()