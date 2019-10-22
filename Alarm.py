# Door alarm program
import time
import os
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

# GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# GPIO.setup(4, GPIO.OUT)
print("Starting")

C1 = 18
C2 = 23
C3 = 24
C4 = 20
C1_last_toggle = time.time()
C2_last_toggle = time.time()
C3_last_toggle = time.time()
C4_last_toggle = time.time()
C1_ship_start = 15
C1_ship_end = 17
C4_switch_timer = time.time()
C4_switch_bool = 0

R1 = 4
R2 = 22
R3 = 6
R4 = 26

GPIO.setup(C1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(C2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(C3, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(C4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(R1, GPIO.OUT)
GPIO.setup(R2, GPIO.OUT)
GPIO.setup(R3, GPIO.OUT)
GPIO.setup(R4, GPIO.OUT)

# clear relays
GPIO.output(R1, False)
GPIO.output(R2, False)
GPIO.output(R3, False)
GPIO.output(R4, False)
    
def toggle_check():
    
    global C1_last_toggle
    global C2_last_toggle
    global C3_last_toggle
    global C1_ship_start
    global C1_ship_end
    global C4_switch_timer
    global C4_switch_bool
    
    if (GPIO.input(C1) == 0):
        GPIO.output(R1, False)
        C1_last_toggle = time.time()
    else:
        GPIO.output(R1, True)
        if (time.time() - C1_last_toggle > 5 and time.localtime().tm_hour < C1_ship_start or time.localtime().tm_hour > C1_ship_end):
            print('C1 Alarm')
        
    if (GPIO.input(C2) == 0):
        GPIO.output(R2, False)
        C2_last_toggle = time.time()
    else:
        GPIO.output(R2, True)
        if (time.time() - C2_last_toggle > 5): 
            print('C2 Alarm')
        
    if (GPIO.input(C3) == 0):
        GPIO.output(R3, False)
        C3_last_toggle = time.time()
    else:
        GPIO.output(R3, True)
        if (time.time() - C3_last_toggle > 5):
            print('C3 Alarm')

    if (GPIO.input(C4) == 0):
        GPIO.output(R4, False)            
    else:
        GPIO.output(R4, True)
        C3_last_toggle = time.time()
        


try:
    print(time.localtime().tm_hour)
    while True:
        toggle_check()
        sleep(0.1)
        
finally: # when your CTRL+C exit, we clean up
    GPIO.cleanup() # clean up all GPIO