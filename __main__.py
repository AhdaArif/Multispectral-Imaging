from gpiozero import DigitalOutputDevice, DigitalInputDevice
from time import sleep

from src import shut, mount

pin = DigitalOutputDevice(18)

while True:
   sleep(3)
   key = input('Take a picture or quit [y/n/m for mount]? > ')
   if key=='y': shut(pin)
   if key=='m': mount(pin)
   elif key=='n': break
   else: continue