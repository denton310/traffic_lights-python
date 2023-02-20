from machine import Pin
from time import sleep

led_red = Pin(2, Pin.OUT)
led_yellow = Pin(3, Pin.OUT)
led_green = Pin(4, Pin.OUT)

led_red.value(0)
led_yellow.value(0)
led_green.value(0)

button1 = Pin(14, Pin.IN, Pin.PULL_DOWN)

interrupt_flag = 0
seconds = 0

# Change mode between LIGHTS_ACTIVE and YELLOW_BLINKING
def callback(button1):
    global interrupt_flag, seconds
    print("button pressed.")
    interrupt_flag = 1
    seconds = 0

button1.irq(trigger=Pin.IRQ_FALLING, handler=callback)

def update_lights():
    global seconds
    print("seconds:", seconds)
    if (seconds < 5):
        led_red.value(0)
        led_yellow.value(0)
        led_green.value(1)

    elif (seconds < 6):
        led_red.value(0)
        led_yellow.value(1)
        led_green.value(0)

    elif (seconds < 11):
        led_red.value(1)
        led_yellow.value(0)
        led_green.value(0)

    elif (seconds < 12):
        led_red.value(1)
        led_yellow.value(1)
        led_green.value(0)

def update_idle():
    global seconds

    if (seconds % 2 == 0):
        led_red.value(0)
        led_yellow.value(1)
        led_green.value(0)
    else:
        led_yellow.value(0)

while True:
    
    if interrupt_flag is 1:
        update_idle()		#this is normal mode
    else:
        update_lights()		#when interrupt are occured

    if(seconds == 11):
        seconds = 0
    else:
        seconds = seconds + 1

    sleep(1)
