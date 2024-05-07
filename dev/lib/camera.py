# auto generated content from camera configuration
from lib.controller import *
import fischertechnik.factories as txt_factory

TXT_M_USB1_1_camera.set_rotate(False)
TXT_M_USB1_1_camera.set_height(240)
TXT_M_USB1_1_camera.set_width(320)
TXT_M_USB1_1_camera.set_fps(30)
TXT_M_USB1_1_camera.start()

color_detector = txt_factory.camera_factory.create_color_detector(15, 32, 295, 124, 1)
TXT_M_USB1_1_camera.add_detector(color_detector)

