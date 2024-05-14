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

m1_pin1 = Pin(22, Pin.OUT)
m1_pin2 = Pin(23, Pin.OUT)
m1_enable = PWM(Pin(27), frequency)

dc_AVD = DCMotor(m1_pin1, m1_pin2, m1_enable)

m2_pin1 = Pin(4, Pin.OUT)
m2_pin2 = Pin(16, Pin.OUT)
m2_enable = PWM(Pin(14), frequency)

dc_ARD = DCMotor(m2_pin1, m2_pin2, m2_enable)

m3_pin1 = Pin(19, Pin.OUT)
m3_pin2 = Pin(18, Pin.OUT)
m3_enable = PWM(Pin(23), frequency)

dc_AVG = DCMotor(m3_pin1, m3_pin2, m3_enable)

m4_pin1 = Pin(2, Pin.OUT)  
m4_pin2 = Pin(15, Pin.OUT)  
m4_enable = PWM(Pin(5), frequency)

dc_ARG = DCMotor(m4_pin1, m4_pin2, m4_enable)
    
    
def Forward() :
    print("Forward") #Avancer
    dc_AVD.one(100)
    dc_ARD.one(100)
    dc_AVG.one(100)
    dc_ARG.one(100)
    
def Backward() :
    print("backward")
    dc_AVD.two(100)
    dc_ARD.two(100)
    dc_AVG.two(100)
    dc_ARG.two(100)
    
def LD() :
    print("LD") #Left_diagonal
    dc_AVD.one(100)
    dc_ARG.one(100)
    sleep(1)
def RD() :
    print("RD") #Right_diagonal
    dc_ARD.one(100)
    dc_AVG.one(100)
    sleep(1)
def RC() :
    print("RC") #rotate clockwise
    dc_AVD.two(100)
    dc_ARD.two(100)
    dc_AVG.one(100)
    dc_ARG.one(100)
    sleep(1)
def RCC() :
    print("RCC") #rotate counter clockwise
    dc_AVD.one(100)
    dc_ARD.one(100)
    dc_AVG.two(100)
    dc_ARG.two(100)
    sleep(1)
def RS() :    
    print("RS") #Right_slide
    dc_AVD.two(100)
    dc_ARD.one(100)
    dc_AVG.one(100)
    dc_ARG.two(100)
    sleep(1)
def LS() :
    print("LS") #left_slide
    dc_AVD.one(100)
    dc_ARD.two(100)
    dc_AVG.two(100)
    dc_ARG.one(100)
    sleep(1)
def RRD() :
    print("RRD") #Reverse_Right_diagonal_
    dc_ARD.two(100)
    dc_AVG.two(100)
    sleep(1)
def RLD() :
    print("RLD") #Reverse_left_diagonal
    dc_AVD.two(100)
    dc_ARG.two(100)
    sleep(1)

def Stop(): 
    dc_AVD.stop()
    dc_ARD.stop()
    dc_AVG.stop()
    dc_ARG.stop()