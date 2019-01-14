from gpiozero import LED
from time import sleep
from pad4pi import rpi_gpio

global led1
led1 = LED(18)
global led2
led2 = LED(10)
global led3
led3 = LED(9)
global led4
led4 = LED(11)
global led5
led5 = LED(8)
global led6
led6 = LED(7)
global led7
led7 = LED(22)
global led8
led8 = LED(27)

KEYPAD = [
    ["1","2","3","A"],
    ["4","5","6","B"],
    ["7","8","9","C"],
    ["*","0","#","D"]
]

rowPins = [16,12,26,19]
colPins = [13,6,5,25]

factory = rpi_gpio.KeypadFactory()

keypad = factory.create_keypad(keypad=KEYPAD, row_pins=rowPins, col_pins=colPins)

def printKey(key):
    print(key)
    if (key == "1" and led1.is_active == False):
        led1.on()
    elif (key == "1" and led1.is_active == True):
        led1.off()
    elif (key == "2" and led2.is_active == False):
        led2.on()
    elif (key == "2" and led2.is_active == True):
        led2.off()
    elif (key == "3" and led3.is_active == False):
        led3.on()
    elif (key == "3" and led3.is_active == True):
        led3.off()
    elif (key == "4" and led4.is_active == False):
        led4.on()
    elif (key == "4" and led4.is_active == True):
        led4.off()
    elif (key == "5" and led5.is_active == False):
        led5.on()
    elif (key == "5" and led5.is_active == True):
        led5.off()
    elif (key == "6" and led6.is_active == False):
        led6.on()
    elif (key == "6" and led6.is_active == True):
        led6.off()
    elif (key == "7" and led7.is_active == False):
        led7.on()
    elif (key == "7" and led7.is_active == True):
        led7.off()
    elif (key == "8" and led8.is_active == False):
        led8.on()
    elif (key == "8" and led8.is_active == True):
        led8.off()

keypad.registerKeyPressHandler(printKey)

try:
    while(True):
        sleep(.05)
except:
     keypad.cleanup()