from gpiozero import LED
from time import sleep
from bottle import route, run, template

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

@route('/lights/<number>')
def index(number):
    if (number == "1" and led1.is_active == False):
        led1.on()
        return template('<b>{{number}} is on</b>!', number=number)
    elif (number == "1" and led1.is_active == True):
        led1.off()
        return template('<b>{{number}} is off</b>!', number=number)
    elif (number == "2" and led2.is_active == False):
        led2.on()
        return template('<b>{{number}} is on</b>!', number=number)
    elif (number == "2" and led2.is_active == True):
        led2.off()
        return template('<b>{{number}} is off</b>!', number=number)
    elif (number == "3" and led3.is_active == False):
        led3.on()
        return template('<b>{{number}} is on</b>!', number=number)
    elif (number == "3" and led3.is_active == True):
        led3.off()
        return template('<b>{{number}} is off</b>!', number=number)
    elif (number == "4" and led4.is_active == False):
        led4.on()
        return template('<b>{{number}} is on</b>!', number=number)
    elif (number == "4" and led4.is_active == True):
        led4.off()
        return template('<b>{{number}} is off</b>!', number=number)
    elif (number == "5" and led5.is_active == False):
        led5.on()
        return template('<b>{{number}} is on</b>!', number=number)
    elif (number == "5" and led5.is_active == True):
        led5.off()
        return template('<b>{{number}} is off</b>!', number=number)
    elif (number == "6" and led6.is_active == False):
        led6.on()
        return template('<b>{{number}} is on</b>!', number=number)
    elif (number == "6" and led6.is_active == True):
        led6.off()
        return template('<b>{{number}} is off</b>!', number=number)
    elif (number == "7" and led7.is_active == False):
        led7.on()
        return template('<b>{{number}} is on</b>!', number=number)
    elif (number == "7" and led7.is_active == True):
        led7.off()
        return template('<b>{{number}} is off</b>!', number=number)
    elif (number == "8" and led8.is_active == False):
        led8.on()
        return template('<b>{{number}} is on</b>!', number=number)
    elif (number == "8" and led8.is_active == True):
        led8.off()
        return template('<b>{{number}} is off</b>!', number=number)
    return template('<b>{{number}}</b>!', number=number)

run(host='localhost', port=5555)
	