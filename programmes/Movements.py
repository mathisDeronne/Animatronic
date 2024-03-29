from machine import Pin, PWM
from time import sleep

class DCMotor:
    def __init__(self, pin1, pin2, enable_pin, min_duty=0, max_duty=1023):
        self.pin1 = pin1
        self.pin2 = pin2
        self.enable_pin = enable_pin
        self.min_duty = min_duty
        self.max_duty = max_duty

    def one(self, speed):
        self.speed = speed
        self.enable_pin.duty(self.duty_cycle(self.speed))
        self.pin1.value(1)
        self.pin2.value(0)
        

    def two(self, speed):
        self.speed = speed
        self.enable_pin.duty(self.duty_cycle(self.speed))
        self.pin1.value(0)
        self.pin2.value(1)

    def stop(self):
        self.enable_pin.duty(0)
        self.pin1.value(0)
        self.pin2.value(0)
        
    def duty_cycle(self, speed):
        if speed <= 0 or speed > 100:
            duty_cycle = 0
        else:
            duty_cycle = int(self.min_duty + (self.max_duty - self.min_duty) * ((speed - 1) / (100 - 1)))
        return duty_cycle

frequency = 1000

m1_pin1 = Pin(26, Pin.OUT)
m1_pin2 = Pin(25, Pin.OUT)
m1_enable = PWM(Pin(27), frequency)

dc_AVD = DCMotor(m1_pin1, m1_pin2, m1_enable)

m2_pin1 = Pin(33, Pin.OUT)
m2_pin2 = Pin(32, Pin.OUT)
m2_enable = PWM(Pin(14), frequency)

dc_ARD = DCMotor(m2_pin1, m2_pin2, m2_enable)


m3_pin1 = Pin(21, Pin.OUT)
m3_pin2 = Pin(19, Pin.OUT)
m3_enable = PWM(Pin(5), frequency)

dc_AVG = DCMotor(m3_pin1, m3_pin2, m3_enable)

m4_pin1 = Pin(23, Pin.OUT)  
m4_pin2 = Pin(22, Pin.OUT)  
m4_enable = PWM(Pin(18), frequency)

dc_ARG = DCMotor(m4_pin1, m4_pin2, m4_enable)
    
    
while True:
    print("Forward") #Avancer
    dc_AVD.one(100)
    dc_ARD.one(100)
    dc_AVG.one(100)
    dc_ARG.one(100)
    print("After motor forward")
    sleep(10)  # Sleep for 1 second (adjust as needed)
    dc_AVD.stop()  # Stop the motors
    dc_ARD.stop()
    dc_AVG.stop()
    dc_ARG.stop()
    sleep(10)
    print("backward")
    dc_AVD.two(100)
    dc_ARD.two(100)
    dc_AVG.two(100)
    dc_ARG.two(100)
    print("After motor backward")
    sleep(10)
    dc_AVD.stop()
    dc_ARD.stop()
    dc_AVG.stop()
    dc_ARG.stop()
    sleep(1)
    print("LD") #Left_diagonal
    dc_AVD.one(100)
    # dc_ARD.two(100)
    # dc_AVG.two(100)
    dc_ARG.one(100)
    print("After motor ")
    sleep(1)
    dc_AVD.stop()
    dc_ARD.stop()
    dc_AVG.stop()
    dc_ARG.stop()
    sleep(1)
    print("RD") #Right_diagonal
    dc_ARD.one(100)
    dc_AVG.one(100)
    print("After motor ")
    sleep(1)
    dc_AVD.stop()
    dc_ARD.stop()
    dc_AVG.stop()
    dc_ARG.stop()
    sleep(1)
    print("RC") #rotate clockwise
    dc_AVD.two(100)
    dc_ARD.two(100)
    dc_AVG.one(100)
    dc_ARG.one(100)
    print("After motor ")
    sleep(1)
    dc_AVD.stop()
    dc_ARD.stop()
    dc_AVG.stop()
    dc_ARG.stop()
    sleep(1)
    print("RCC") #rotate counter clockwise
    dc_AVD.one(100)
    dc_ARD.one(100)
    dc_AVG.two(100)
    dc_ARG.two(100)
    print("After motor ")
    sleep(1)
    dc_AVD.stop()
    dc_ARD.stop()
    dc_AVG.stop()
    dc_ARG.stop()
    sleep(1)
    print("RS") #Right_slide
    dc_AVD.two(100)
    dc_ARD.one(100)
    dc_AVG.one(100)
    dc_ARG.two(100)
    print("After motor ")
    sleep(1)
    dc_AVD.stop()
    dc_ARD.stop()
    dc_AVG.stop()
    dc_ARG.stop()
    sleep(1)
    print("LS") #left_slide
    dc_AVD.one(100)
    dc_ARD.two(100)
    dc_AVG.two(100)
    dc_ARG.one(100)
    print("After motor ")
    sleep(1)
    dc_AVD.stop()
    dc_ARD.stop()
    dc_AVG.stop()
    dc_ARG.stop()
    sleep(1)
    print("RRD") #Reverse_Right_diagonal_
    dc_ARD.two(100)
    dc_AVG.two(100)
    print("After motor ")
    sleep(1)
    dc_AVD.stop()
    dc_ARD.stop()
    dc_AVG.stop()
    dc_ARG.stop()
    sleep(1)
    print("RLD") #Reverse_left_diagonal
    dc_AVD.two(100)
    dc_ARG.two(100)
    print("After motor ")
    sleep(1)
    dc_AVD.stop()
    dc_ARD.stop()
    dc_AVG.stop()
    dc_ARG.stop()
    sleep(1)