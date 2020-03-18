import RPi.GPIO as gpio
import time

#BCM PINS ON RASPBERRYPI
lForward = 20
lBackward = 21
lm = 16

rForward = 19 
rBackward = 26
rm = 13

gpio.setmode(gpio.BCM)

#gpio.setwarnings(False)

def motor_int():
    global speed_ena
    global speed_enb
    global delaytime
    gpio.setup(lm, gpio.OUT, initial=gpio.HIGH)
    gpio.setup(lForward, gpio.OUT, initial=gpio.LOW)
    gpio.setup(lBackward, gpio.OUT, initial=gpio.LOW)
    gpio.setup(rm, gpio.OUT, initial=gpio.HIGH)
    gpio.setup(rForward, gpio.OUT, initial=gpio.LOW)
    gpio.setup(rBackward, gpio.OUT, initial=gpio.LOW)
    speed_ena = gpio.PWM(lm, 2000)
    speed_enb = gpio.PWM(rm, 2000)
    speed_ena.start(0)
    speed_enb.start(0)

def run(delaytime):
    gpio.output(lForward, gpio.HIGH)
    gpio.output(lBackward, gpio.LOW)
    gpio.output(rForward, gpio.HIGH)
    gpio.output(rBackward, gpio.LOW)
    speed_ena.ChangeDutyCycle(50)
    speed_enb.ChangeDutyCycle(50)
    time.sleep(delaytime)

def pivot(delaytime):
    gpio.output(lForward, gpio.LOW)
    gpio.output(lBackward, gpio.LOW)
    gpio.output(rForward, gpio.LOW)
    gpio.output(rBackward, gpio.LOW)
    speed_ena.ChangeDutyCycle(0)
    speed_enb.ChangeDutyCycle(0)
    time.sleep(delaytime)

def leftturn(delaytime):
    gpio.output(lForward, gpio.LOW)
    gpio.output(lBackward, gpio.LOW)
    gpio.output(rForward, gpio.HIGH)
    gpio.output(rBackward, gpio.LOW)
    speed_ena.ChangeDutyCycle(00)
    speed_enb.ChangeDutyCycle(50)
    time.sleep(delaytime)


try:
    motor_int()
    while True:
        run(1)
        pivot(1)
        leftturn(3.85)
        pivot(1)
except KeyboardInterrupt:   
    pass
speed_ena.stop()
gpio.cleanup()