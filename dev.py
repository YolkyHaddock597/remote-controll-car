from machine import Pin, PWM
import utime
import _thread
import urequests
import ujson
import network
import socket
from time import sleep

import stepper

ssid = ''
password = ''

def connect():
    #Connect to WLAN
    print("CONNECT")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
        
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print(wlan.ifconfig())

connect()

s1 = stepper.create(Pin(1,Pin.OUT),Pin(2,Pin.OUT),Pin(3,Pin.OUT),Pin(4,Pin.OUT),Pin(5,Pin.OUT),Pin(6,Pin.OUT),Pin(7,Pin.OUT),Pin(8,Pin.OUT), delay=2)
state = 5
def api_call(state):
    global direct
    direct = "none"
    if state == 1:
        state = 5
        return state
    response = urequests.get("")
    parsed = ujson.loads(response.content)
    print(parsed)
    if parsed['direction'] == 2 and parsed['forwards'] == 1:
        direct = "foward"
    elif parsed['direction'] == 1 and parsed['forwards'] == 1:
        direct = "left"
    elif parsed['direction'] == 0 and parsed['forwards'] == 1:
        direct = "right"
    elif parsed['direction'] == 0 and parsed['forwards'] == 0:
        direct = "stop"
    return direct



#s1.step(-10000)
pwm = PWM(Pin(0))
pwm.freq(50)


#Function to set an angle
#The position is expected as a parameter

def setServoCycle (position):
    pwm.duty_u16(position)
    sleep(0.01)

while True:
    api_call(state)
    state = state - 1
    if direct == "foward":
        setServoCycle(6400)
        s1.step(-100)
    elif direct == "left":
        setServoCycle(5550)
        s1.step(-100)
    elif direct == "right":
        setServoCycle(8000)
        s1.step(-100)
    elif direct == "stop":
        setServoCycle(6400)
        
        

#while True:
    #for pos in range(1000,9000,50):
        #setServoCycle(pos)
    #for pos in range(9000,1000,-50):
        #setServoCycle(pos)
# while True:
# #center
#     sleep(1)
#     setServoCycle(6400)
#     sleep(1)
# 
#     setServoCycle(5550)
#     sleep(1)
# 
#     setServoCycle(8000)



