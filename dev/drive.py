import time
from fischertechnik.controller.Motor import Motor
from lib.camera import *
from lib.Color import *
from lib.controller import *
from lib.display import *

def color_callback(event):
    if display.get_attr("txt_checkbox.checked"):
        if event.value.get_rgb_red() > 130 and event.value.get_rgb_green() < 140:
            #TXT_M.get_loudspeaker().play("26_Augenzwinkern.wav", False)
            TXT_M_S1_servomotor.set_position(int(330))
            time.sleep(1)
            TXT_M_S1_servomotor.set_position(int(256))
            display.set_attr("farbe.text", "rot")
        if event.value.get_rgb_red() < 130 and event.value.get_rgb_green() > 135:
            #TXT_M.get_loudspeaker().play("01_Airplane.wav", False)
            TXT_M_S1_servomotor.set_position(int(170))
            time.sleep(1)
            TXT_M_S1_servomotor.set_position(int(256))
            display.set_attr("farbe.text", "grün")
    print("farbe!!!")

color_detector.add_detection_listener(color_callback)


while True:
    display.set_attr("vorne.text", str(TXT_M_I1_ultrasonic_distance_meter.get_distance()))
    display.set_attr("rechts.text", str(TXT_M_I3_ultrasonic_distance_meter.get_distance()))
    display.set_attr("links.text", str(TXT_M_I2_ultrasonic_distance_meter.get_distance()))
    display.set_attr("hinten.text", str(TXT_M_I4_ultrasonic_distance_meter.get_distance()))
    print (display.get_attr("start.checked"))
    if display.get_attr("start.checked"):
        maxLegitDistance = 1000
        if TXT_M_I1_ultrasonic_distance_meter.get_distance() > maxLegitDistance or TXT_M_I2_ultrasonic_distance_meter.get_distance() > maxLegitDistance or  TXT_M_I3_ultrasonic_distance_meter.get_distance() > maxLegitDistance or TXT_M_I4_ultrasonic_distance_meter.get_distance() > maxLegitDistance or TXT_M_I5_ultrasonic_distance_meter.get_distance() > maxLegitDistance or TXT_M_I6_ultrasonic_distance_meter.get_distance() > maxLegitDistance:
            print("Sensor Failed")
           # TXT_M.get_loudspeaker().play("02_Alarm.wav", False)
        TXT_M_S1_servomotor.set_position(int(256))
        TXT_M_M1_motor.set_speed(int(325), Motor.CW)
        TXT_M_M1_motor.start()
        TXT_M_S1_servomotor.set_position(int(256))
        if TXT_M_I2_ultrasonic_distance_meter.get_distance() < 25:
            TXT_M_S1_servomotor.set_position(int(170))
            time.sleep(1)
            TXT_M_S1_servomotor.set_position(int(256))
        if TXT_M_I3_ultrasonic_distance_meter.get_distance() < 25:
            TXT_M_S1_servomotor.set_position(int(330))
            time.sleep(1)
            TXT_M_S1_servomotor.set_position(int(256))
        if TXT_M_I1_ultrasonic_distance_meter.get_distance() < 83:
            if TXT_M_I3_ultrasonic_distance_meter.get_distance() < (TXT_M_I2_ultrasonic_distance_meter.get_distance()):
                TXT_M_S1_servomotor.set_position(int(330))
                time.sleep(1)
                TXT_M_S1_servomotor.set_position(int(256))
            else:
                TXT_M_S1_servomotor.set_position(int(170))
                time.sleep(1)
                TXT_M_S1_servomotor.set_position(int(256))
        # Vorne und Vorne Schräg
        if (TXT_M_I1_ultrasonic_distance_meter.get_distance() < 30) or (TXT_M_I5_ultrasonic_distance_meter.get_distance() < 15) or (TXT_M_I6_ultrasonic_distance_meter.get_distance() < 15):
            TXT_M_M1_motor.set_speed(int(0), Motor.CW)
            TXT_M_M1_motor.start()
            TXT_M_M1_motor.set_speed(int(325), Motor.CCW)
            TXT_M_M1_motor.start()
            TXT_M_S1_servomotor.set_position(int(256))
            time.sleep(1)
            if TXT_M_I3_ultrasonic_distance_meter.get_distance() < (TXT_M_I2_ultrasonic_distance_meter.get_distance()):
                TXT_M_S1_servomotor.set_position(int(170))
                time.sleep(1)
                TXT_M_S1_servomotor.set_position(int(256))
            else:
                TXT_M_S1_servomotor.set_position(int(330))
                time.sleep(1)
                TXT_M_S1_servomotor.set_position(int(256))
        if TXT_M_I4_ultrasonic_distance_meter.get_distance() < 15:
            TXT_M_M1_motor.set_speed(int(0), Motor.CCW)
            TXT_M_M1_motor.start()
            time.sleep(1)
            TXT_M_M1_motor.set_speed(int(325), Motor.CW)
            TXT_M_M1_motor.start()
