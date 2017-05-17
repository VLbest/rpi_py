import time

from MyConstants import *
from ArdSender import ArdSender
from KeyboardListenner import KeyboardListenner
from Motor import Motor


class DriveController():
    def __init__(self):
        self.Keyboard = KeyboardListenner()
        self.LeftDrive = Motor(Sides.Left)
        self.RightDrive = Motor(Sides.Right)

    def goForward(self):

        if ((self.LeftDrive.Direction == Directions.Backward or self.RightDrive.Direction == Directions.Backward) and
            (self.LeftDrive.Speed == Speeds.Max or self.RightDrive.Speed == Speeds.Max)):
            ArdSender.sendCommand(100, "Stop turning")
            time.sleep(0.5)


        if self.LeftDrive.Speed == -1 or self.RightDrive.Speed == -1:
            self.RightDrive.Speed == Speeds.Normal
            self.LeftDrive.Speed == Speeds.Normal
            ArdSender.sendCommand(64, "Init_left_speed")
            ArdSender.sendCommand(74, "Init_right_speed")

        self.LeftDrive.Direction = Directions.Forward
        self.RightDrive.Direction = Directions.Forward
        ArdSender.sendCommand(20, "Left_Go_Forward")
        ArdSender.sendCommand(30, "Right_Go_Forward")
        ArdSender.sendCommand(20, "Left_Go_Forward_Rewrite")
        ArdSender.sendCommand(30, "Right_Go_Forward_Rewrite")


    def goBackward(self):

        if ((self.LeftDrive.Direction == Directions.Forward or self.RightDrive.Direction == Directions.Forward) and
                (self.LeftDrive.Speed == Speeds.Max or self.RightDrive.Speed == Speeds.Max)):
            ArdSender.sendCommand(100, "Stop turning")
            time.sleep(0.5)


        if self.LeftDrive.Speed == -1 or self.RightDrive.Speed == -1:
            self.RightDrive.Speed == Speeds.Normal
            self.LeftDrive.Speed == Speeds.Normal
            ArdSender.sendCommand(64, "Init_left_speed")
            ArdSender.sendCommand(74, "Init_right_speed")

        self.LeftDrive.Direction = Directions.Backward
        self.RightDrive.Direction = Directions.Backward
        ArdSender.sendCommand(40, "Left_Go_Backward")
        ArdSender.sendCommand(50, "Right_Go_Backward")
        ArdSender.sendCommand(40, "Left_Go_Backward_Rewrite")
        ArdSender.sendCommand(50, "Right_Go_Backward_Rewrite")



    def goForwardLeft(self):
        self.LeftDrive.Direction = Directions.Forward
        ArdSender.sendCommand(20, "Left_Go_Forward")

    def goBackwardLeft(self):
        self.LeftDrive.Direction = Directions.Backward
        ArdSender.sendCommand(40, "Left_Go_Backward")

    def goForwardRigth(self):
        self.RightDrive.Direction = Directions.Forward
        ArdSender.sendCommand(30, "Right_Go_Forward")

    def goBackwardRight(self):
        self.RightDrive.Direction = Directions.Backward
        ArdSender.sendCommand(50, "Right_Go_Backward")

    def TurnOffEverything(self):
        self.LeftDrive.Speed = 0
        self.RightDrive.Speed = 0
        ArdSender.sendCommand(100, "Turn Engine OFF")

    def SetLeftSpeedVerySlow(self):
        self.LeftDrive.Speed = Speeds.VerySlow
        self.LeftDrive.Speed = Speeds.VerySlow
        ArdSender.sendCommand(60, "Set_Left_Speed = Very Slow")
        self.applySpeed(self.LeftDrive)

    def SetLeftSpeedSlow(self):
        self.LeftDrive.Speed = Speeds.Slow
        ArdSender.sendCommand(62, "Set_Left_Speed = Slow")
        self.applySpeed(self.LeftDrive)

    def SetLeftSpeedNormal(self):
        self.LeftDrive.Speed = Speeds.Normal
        ArdSender.sendCommand(64, "Set_Left_Speed = Normal")
        self.applySpeed(self.LeftDrive)

    def SetLeftSpeedFast(self):
        self.LeftDrive.Speed = Speeds.Fast
        ArdSender.sendCommand(66, "Set_Left_Speed = Fast")
        self.applySpeed(self.LeftDrive)

    def SetLeftSpeedMax(self):
        self.LeftDrive.Speed = Speeds.Max
        ArdSender.sendCommand(68, "Set_Left_Speed Max")
        self.applySpeed(self.LeftDrive)

    def SetRightSpeedVerySlow(self):
        self.RightDrive.Speed = Speeds.VerySlow
        ArdSender.sendCommand(70, "Set_Right_Speed = Very Slow")
        self.applySpeed(self.RightDrive)

    def SetRightSpeedSlow(self):
        self.RightDrive.Speed = Speeds.Slow
        ArdSender.sendCommand(72, "Set_Right_Speed = Slow")
        self.applySpeed(self.RightDrive)

    def SetRightSpeedNormal(self):
        self.RightDrive.Speed = Speeds.Normal
        ArdSender.sendCommand(74, "Set_Right_Speed = Normal")
        self.applySpeed(self.RightDrive)

    def SetRightSpeedFast(self):
        self.LeftDrive.Speed = Speeds.Fast
        ArdSender.sendCommand(76, "Set_Right_Speed = Fast")
        self.applySpeed(self.RightDrive)

    def SetRightSpeedMax(self):
        self.LeftDrive.Speed = Speeds.Max
        ArdSender.sendCommand(78, "Set_Right_Speed Max")
        self.applySpeed(self.RightDrive)

    def TurnToLeft(self):
        #self.TurnOffEverything()
        #self.SetLeftSpeedMax()
        #self.SetRightSpeedMax()
        self.SetSpeedMax()
        self.goBackwardLeft()
        self.goForwardRigth()
        time.sleep(0.1)
        ArdSender.sendCommand(100, "Stop turning")
        self.LeftDrive.Speed = -1
        self.RightDrive.Speed = -1


    def TurnToRight(self):
        self.SetSpeedMax()
        self.goForwardLeft()
        self.goBackwardRight()
        time.sleep(0.1)
        ArdSender.sendCommand(100, "Stop turning")
        self.LeftDrive.Speed = -1
        self.RightDrive.Speed = -1


    def applySpeed(self, Drive):
        if Drive.Direction == Directions.Forward and Drive.Side == Sides.Left:
            ArdSender.sendCommand(20, "Apply_Speed_Forward_Left")
        if Drive.Direction == Directions.Forward and Drive.Side == Sides.Right:
            ArdSender.sendCommand(30, "Apply_Speed_Forward_Right")
        if Drive.Direction == Directions.Backward and Drive.Side == Sides.Left:
            ArdSender.sendCommand(40, "Apply_Speed_Backward_Left")
        if Drive.Direction == Directions.Backward and Drive.Side == Sides.Right:
            ArdSender.sendCommand(50, "Apply_Speed_Backward_Right")

    def SetSpeedVerySlow(self):
        self.SetLeftSpeedVerySlow()
        self.SetRightSpeedVerySlow()

    def SetSpeedSlow(self):
        self.SetLeftSpeedSlow()
        self.SetRightSpeedSlow()

    def SetSpeedNormal(self):
        self.SetLeftSpeedNormal()
        self.SetRightSpeedNormal()

    def SetSpeedMax(self):
        self.SetLeftSpeedMax()
        self.SetRightSpeedMax()
