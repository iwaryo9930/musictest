from pygame import mixer
import RPi.GPIO as GPIO
from time import sleep

def my_callback(channel):
    global btnState
    global pauseState
    if channel==27 and pauseState%2==0:
        btnState = not btnState
        if btnState==GPIO.HIGH:
           mixer.music.unpause()
           pauseState = pauseState+1
    elif channel==27:
        btnState = not btnState
        if btnState==GPIO.HIGH:
            mixer.init()
            mixer.music.load("Lofi.mp3")
            mixer.music.play(-1)
        else:
            mixer.music.pause()
            pauseState = pauseState+1
            

GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(27,GPIO.RISING,callback=my_callback,bouncetime=200)

btnState=GPIO.LOW
pauseState=1

try:
    while True:
        sleep(0.01)

except KeyboardInterrupt:
    pass

GPIO.cleanup()

            




