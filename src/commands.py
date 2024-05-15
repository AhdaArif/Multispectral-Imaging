from gpiozero import DigitalOutputDevice as dod
from time import sleep

def pulse (pin:dod, width:float):
   assert width in (1.5e-3, 2.0e-3), "Pulse command's not recognized"
   pin.off()
   sleep(1.0e-3)
   pin.on()
   sleep(width)
   pin.off()

mount = lambda pin: pulse(pin, 1.5e-3)
shut = lambda pin: pulse(pin, 2.0e-3)