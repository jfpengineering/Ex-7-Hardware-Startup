import time

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix import label
from kivy.uix.screenmanager import ScreenManager, Screen
from pidev.kivy import DPEAButton
from pidev.kivy import ImageButton
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.animation import Animation
from threading import Thread
from time import sleep
import spidev
import os
from time import sleep
import RPi.GPIO as GPIO
from pidev.stepper import stepper
from pidev.Cyprus_Commands import Cyprus_Commands_RPi as cyprus
from Slush.Devices import L6470Registers
spi = spidev.SpiDev()

# Init a 200 steps per revolution stepper on Port 0
s0 = stepper(port=0, micro_steps=32, hold_current=20, run_current=20, accel_current=20, deaccel_current=20,
             steps_per_unit=200, speed=8)

SCREEN_MANAGER = ScreenManager()
MAIN_SCREEN_NAME = 'main'

class ProjectNameGUI(App):

    def build(self):
        return SCREEN_MANAGER

Window.clearcolor = (0, 1, 0, 1)

class MainScreen(Screen):

    counter_btn = ObjectProperty(None)
    toggle_label = ObjectProperty(None)
    dir_btn = ObjectProperty(None)
    dir_label = ObjectProperty(None)
    slider = ObjectProperty(None)
    stop_btn = ObjectProperty(None)
    pos_label = ObjectProperty(None)
    the_btn = ObjectProperty(None)
    switch_label = ObjectProperty(None)

    @staticmethod
    def stop():
        s0.stop()

    def servo_move(self):
        cyprus.initialize()
        cyprus.setup_servo(1)
        cyprus.set_servo_position(1,0)
        cyprus.close()

    def limit_switch(self):
        cyprus.initialize()
        cyprus.setup_servo(1)
        while True:
            if (cyprus.read_gpio() & 0b0001):  # binary bitwise AND of the value returned from read.gpio()
                #sleep(1)
                if (cyprus.read_gpio() & 0b0001):  # a little debounce logic
                    self.switch_label.text = "GPIO on port P6 is HIGH"
                    cyprus.set_servo_position(1, 0)
            else:
                self.switch_label.text = "GPIO on port P6 is LOW"
                cyprus.set_servo_position(1, 1)
                #sleep(1)
        cyprus.close()

    def on_off(self):
        self.dir_label.text = ""

        if self.toggle_label.text == "OFF":
            s0.run(0, 300)
            self.toggle_label.text = "ON"
        else:
            s0.stop()
            self.toggle_label.text = "OFF"

    def toggle_dir(self):
        if self.dir_label.text == "Clockwise":
            s0.run(1, 300)
            self.dir_label.text = "Counter Clockwise"
        elif self.dir_label.text == "Counter Clockwise":
            s0.run(0, 300)
            self.dir_label.text = "Clockwise"
        else:
            s0.run(1, 300)
            self.dir_label.text = "Counter Clockwise"

    def the_fn(self):
        self.pos_label.text = "Current Position: " + str(s0.get_position_in_units())
        s0.go_until_press(1, 1*6400)
        time.sleep(15)
        self.pos_label.text = "Current Position: " + str(s0.get_position_in_units())
        time.sleep(10)
        s0.go_until_press(1, 5*6400)
        time.sleep(2)
        self.pos_label.text = "Current Position: " + str(s0.get_position_in_units())
        time.sleep(8)
        s0.goHome()
        time.sleep(30)
        self.pos_label.text = "Current Position: " + str(s0.get_position_in_units())
        s0.go_until_press(0, 8*6400)
        time.sleep(12.5)
        self.pos_label.text = "Current Position: " + str(s0.get_position_in_units())
        time.sleep(10)
        s0.goHome()
        self.pos_label.text = "Current Position: " + str(s0.get_position_in_units())

    def start_thread1(self):  # This should be inside the MainScreen Class
        Thread(target=self.the_fn).start()

    def start_thread2(self):
        Thread(target=self.limit_switch).start()

    def slide(self):
        if int(self.slider.value) == 0:
            s0.stop()
        elif int(self.slider.value) == 1:
            s0.run(0, 1)
        elif int(self.slider.value) == 2:
            s0.run(0, 2)
        elif int(self.slider.value) == 3:
            s0.run(0, 3)
        elif int(self.slider.value) == 4:
            s0.run(0, 4)
        elif int(self.slider.value) == 5:
            s0.run(0, 5)
        elif int(self.slider.value) == 6:
            s0.run(0, 6)
        elif int(self.slider.value) == 7:
            s0.run(0, 7)
        elif int(self.slider.value) == 8:
            s0.run(0, 8)
        elif int(self.slider.value) == 9:
            s0.run(0, 9)
        elif int(self.slider.value) == 10:
            s0.run(0, 10)
        elif int(self.slider.value) == 11:
            s0.run(0, 11)
        elif int(self.slider.value) == 12:
            s0.run(0, 12)
        elif int(self.slider.value) == 13:
            s0.run(0, 13)
        elif int(self.slider.value) == 14:
            s0.run(0, 14)
        elif int(self.slider.value) == 15:
            s0.run(0, 15)
        elif int(self.slider.value) == 16:
            s0.run(0, 16)
        elif int(self.slider.value) == 17:
            s0.run(0, 17)
        elif int(self.slider.value) == 18:
            s0.run(0, 18)
        elif int(self.slider.value) == 19:
            s0.run(0, 19)
        elif int(self.slider.value) == 20:
            s0.run(0, 20)
        elif int(self.slider.value) == 21:
            s0.run(0, 21)
        elif int(self.slider.value) == 22:
            s0.run(0, 22)
        elif int(self.slider.value) == 23:
            s0.run(0, 23)
        elif int(self.slider.value) == 24:
            s0.run(0, 24)
        elif int(self.slider.value) == 25:
            s0.run(0, 25)
        elif int(self.slider.value) == 26:
            s0.run(0, 26)
        elif int(self.slider.value) == 27:
            s0.run(0, 27)
        elif int(self.slider.value) == 28:
            s0.run(0, 28)
        elif int(self.slider.value) == 29:
            s0.run(0, 29)
        elif int(self.slider.value) == 30:
            s0.run(0, 30)
        elif int(self.slider.value) == 31:
            s0.run(0, 31)
        elif int(self.slider.value) == 32:
            s0.run(0, 32)
        elif int(self.slider.value) == 33:
            s0.run(0, 33)
        elif int(self.slider.value) == 34:
            s0.run(0, 34)
        elif int(self.slider.value) == 35:
            s0.run(0, 35)
        elif int(self.slider.value) == 36:
            s0.run(0, 36)
        elif int(self.slider.value) == 37:
            s0.run(0, 37)
        elif int(self.slider.value) == 38:
            s0.run(0, 38)
        elif int(self.slider.value) == 39:
            s0.run(0, 39)
        elif int(self.slider.value) == 40:
            s0.run(0, 40)
        elif int(self.slider.value) == 41:
            s0.run(0, 41)
        elif int(self.slider.value) == 42:
            s0.run(0, 42)
        elif int(self.slider.value) == 43:
            s0.run(0, 43)
        elif int(self.slider.value) == 44:
            s0.run(0, 44)
        elif int(self.slider.value) == 45:
            s0.run(0, 45)
        elif int(self.slider.value) == 46:
            s0.run(0, 46)
        elif int(self.slider.value) == 47:
            s0.run(0, 47)
        elif int(self.slider.value) == 48:
            s0.run(0, 48)
        elif int(self.slider.value) == 49:
            s0.run(0, 49)
        elif int(self.slider.value) == 50:
            s0.run(0, 50)
        elif int(self.slider.value) == 51:
            s0.run(0, 51)
        elif int(self.slider.value) == 52:
            s0.run(0, 52)
        elif int(self.slider.value) == 53:
            s0.run(0, 53)
        elif int(self.slider.value) == 54:
            s0.run(0, 54)
        elif int(self.slider.value) == 55:
            s0.run(0, 55)
        elif int(self.slider.value) == 56:
            s0.run(0, 56)
        elif int(self.slider.value) == 57:
            s0.run(0, 57)
        elif int(self.slider.value) == 58:
            s0.run(0, 58)
        elif int(self.slider.value) == 59:
            s0.run(0, 59)
        elif int(self.slider.value) == 60:
            s0.run(0, 60)
        elif int(self.slider.value) == 61:
            s0.run(0, 61)
        elif int(self.slider.value) == 62:
            s0.run(0, 62)
        elif int(self.slider.value) == 63:
            s0.run(0, 63)
        elif int(self.slider.value) == 64:
            s0.run(0, 64)
        elif int(self.slider.value) == 65:
            s0.run(0, 65)
        elif int(self.slider.value) == 66:
            s0.run(0, 66)
        elif int(self.slider.value) == 67:
            s0.run(0, 67)
        elif int(self.slider.value) == 68:
            s0.run(0, 68)
        elif int(self.slider.value) == 69:
            s0.run(0, 69)
        elif int(self.slider.value) == 70:
            s0.run(0, 70)
        elif int(self.slider.value) == 71:
            s0.run(0, 71)
        elif int(self.slider.value) == 72:
            s0.run(0, 72)
        elif int(self.slider.value) == 73:
            s0.run(0, 73)
        elif int(self.slider.value) == 74:
            s0.run(0, 74)
        elif int(self.slider.value) == 75:
            s0.run(0, 75)
        elif int(self.slider.value) == 76:
            s0.run(0, 76)
        elif int(self.slider.value) == 77:
            s0.run(0, 77)
        elif int(self.slider.value) == 78:
            s0.run(0, 78)
        elif int(self.slider.value) == 79:
            s0.run(0, 79)
        elif int(self.slider.value) == 80:
            s0.run(0, 80)
        elif int(self.slider.value) == 81:
            s0.run(0, 81)
        elif int(self.slider.value) == 82:
            s0.run(0, 82)
        elif int(self.slider.value) == 83:
            s0.run(0, 83)
        elif int(self.slider.value) == 84:
            s0.run(0, 84)
        elif int(self.slider.value) == 85:
            s0.run(0, 85)
        elif int(self.slider.value) == 86:
            s0.run(0, 86)
        elif int(self.slider.value) == 87:
            s0.run(0, 87)
        elif int(self.slider.value) == 88:
            s0.run(0, 88)
        elif int(self.slider.value) == 89:
            s0.run(0, 89)
        elif int(self.slider.value) == 90:
            s0.run(0, 90)
        elif int(self.slider.value) == 91:
            s0.run(0, 91)
        elif int(self.slider.value) == 92:
            s0.run(0, 92)
        elif int(self.slider.value) == 93:
            s0.run(0, 93)
        elif int(self.slider.value) == 94:
            s0.run(0, 94)
        elif int(self.slider.value) == 95:
            s0.run(0, 95)
        elif int(self.slider.value) == 96:
            s0.run(0, 96)
        elif int(self.slider.value) == 97:
            s0.run(0, 97)
        elif int(self.slider.value) == 98:
            s0.run(0, 98)
        elif int(self.slider.value) == 99:
            s0.run(0, 99)
        else:
            s0.run(0, 100)



Builder.load_file('main.kv')
SCREEN_MANAGER.add_widget(MainScreen(name=MAIN_SCREEN_NAME))

if __name__ == "__main__":
    ProjectNameGUI().run()

s0.free_all()
spi.close()
GPIO.cleanup()