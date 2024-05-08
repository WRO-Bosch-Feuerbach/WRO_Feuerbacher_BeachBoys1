#------ imports ------
import time
from fischertechnik.controller.Motor import Motor
from lib.camera import *
from lib.Color import *
from lib.controller import *
from lib.display import *

#------ variables ------
neutral = None
links = None
rechts = None
lenkzeit = None
geschwindigkeit = None

#------ functions ------
    # setDisplay to set the different display elements and thier values
def setDisplay():
    global neutral, links, rechts, lenkzeit, geschwindigkeit
    display.set_attr("i1Valie.text", str(TXT_M_I1_ultrasonic_distance_meter.get_distance()))
    display.set_attr("i2Value.text", str(TXT_M_I2_ultrasonic_distance_meter.get_distance()))
    display.set_attr("i3Value.text", str(TXT_M_I3_ultrasonic_distance_meter.get_distance()))
    display.set_attr("i4Value.text", str(TXT_M_I4_ultrasonic_distance_meter.get_distance()))
    display.set_attr("i5Value2.text", str(TXT_M_I5_ultrasonic_distance_meter.get_distance()))
    display.set_attr("i6Valpue.text", str(TXT_M_I6_ultrasonic_distance_meter.get_distance()))

    # color_callback to check the color of an object and move/steer the robot accordingly
def color_callback(event):
    global neutral, links, rechts, lenkzeit, geschwindigkeit
    if display.get_attr("txt_checkbox.checked"):
        if event.value.get_rgb_red() > 130 and event.value.get_rgb_green() < 140:
            TXT_M_S1_servomotor.set_position(int(rechts))
            time.sleep(lenkzeit)
            TXT_M_S1_servomotor.set_position(int(256))
            display.set_attr("farbe.text", "rot")
            print("rot")
        if event.value.get_rgb_red() < 130 and event.value.get_rgb_green() > 135:
            TXT_M_S1_servomotor.set_position(int(links))
            time.sleep(lenkzeit)
            TXT_M_S1_servomotor.set_position(int(256))
            display.set_attr("farbe.text", "grün")
            print("grün")

#------ main ------
color_detector.add_detection_listener(color_callback)

neutral = 256
links = 170
rechts = 330
while True:
    setDisplay()
    if display.get_attr("start.checked"):
        if display.get_attr("txt_checkbox.checked"):
            lenkzeit = 0.8
            geschwindigkeit = 375
        else:
            lenkzeit = 0.5
            geschwindigkeit = 500
        TXT_M_S1_servomotor.set_position(int(256))
        TXT_M_M1_motor.set_speed(int(geschwindigkeit), Motor.CW)
        TXT_M_M1_motor.start()
        TXT_M_S1_servomotor.set_position(int(256))
        if TXT_M_I2_ultrasonic_distance_meter.get_distance() < 25:
            TXT_M_S1_servomotor.set_position(int(links))
            time.sleep(lenkzeit)
            TXT_M_S1_servomotor.set_position(int(neutral))
        if TXT_M_I3_ultrasonic_distance_meter.get_distance() < 25:
            TXT_M_S1_servomotor.set_position(int(rechts))
            time.sleep(lenkzeit)
            TXT_M_S1_servomotor.set_position(int(neutral))
        if TXT_M_I1_ultrasonic_distance_meter.get_distance() < 83:
            if TXT_M_I3_ultrasonic_distance_meter.get_distance() < (TXT_M_I2_ultrasonic_distance_meter.get_distance()):
                TXT_M_S1_servomotor.set_position(int(rechts))
                time.sleep(lenkzeit)
                TXT_M_S1_servomotor.set_position(int(neutral))
            else:
                TXT_M_S1_servomotor.set_position(int(links))
                time.sleep(lenkzeit)
                TXT_M_S1_servomotor.set_position(int(neutral))
        # Vorne und Vorne Schräg
        if (TXT_M_I1_ultrasonic_distance_meter.get_distance() < 30) or (TXT_M_I5_ultrasonic_distance_meter.get_distance() < 15) or (TXT_M_I6_ultrasonic_distance_meter.get_distance() < 15):
            TXT_M_M1_motor.set_speed(int(0), Motor.CW)
            TXT_M_M1_motor.start()
            TXT_M_M1_motor.set_speed(int(geschwindigkeit), Motor.CCW)
            TXT_M_M1_motor.start()
            TXT_M_S1_servomotor.set_position(int(neutral))
            time.sleep(lenkzeit)
            if TXT_M_I3_ultrasonic_distance_meter.get_distance() < (TXT_M_I2_ultrasonic_distance_meter.get_distance()):
                TXT_M_S1_servomotor.set_position(int(links))
                time.sleep(lenkzeit)
                TXT_M_S1_servomotor.set_position(int(neutral))
            else:
                TXT_M_S1_servomotor.set_position(int(rechts))
                time.sleep(lenkzeit)
                TXT_M_S1_servomotor.set_position(int(neutral))
            TXT_M_S1_servomotor.set_position(int(neutral))
            if TXT_M_I4_ultrasonic_distance_meter.get_distance() < 15:
                TXT_M_M1_motor.set_speed(int(0), Motor.CCW)
                TXT_M_M1_motor.start()
                time.sleep(lenkzeit)
                TXT_M_M1_motor.set_speed(int(geschwindigkeit), Motor.CW)
                TXT_M_M1_motor.start()
