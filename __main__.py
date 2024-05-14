from gpiozero import OutputDevice
from time import sleep

def setup ():
   trigger = OutputDevice(18)
   

def loop ():
   pass

def main ():
   setup()
   while True: loop()

if __name__=='__main__': main()