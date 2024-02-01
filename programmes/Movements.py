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

m1_pin1 = Pin(19, Pin.OUT)
m1_pin2 = Pin(21, Pin.OUT)
m1_enable = PWM(Pin(12), frequency)

dc_motor1 = DCMotor(m1_pin1, m1_pin2, m1_enable)

m2_pin1 = Pin(23, Pin.OUT)
m2_pin2 = Pin(22, Pin.OUT)
m2_enable = PWM(Pin(14), frequency)

dc_motor2 = DCMotor(m2_pin1, m2_pin2, m2_enable)


m3_pin1 = Pin(27, Pin.OUT)
m3_pin2 = Pin(26, Pin.OUT)
m3_enable = PWM(Pin(25), frequency)

dc_motor3 = DCMotor(m3_pin1, m3_pin2, m3_enable)

m4_pin1 = Pin(18, Pin.OUT)  
m4_pin2 = Pin(5, Pin.OUT)  
m4_enable = PWM(Pin(17), frequency)

dc_motor4 = DCMotor(m4_pin1, m4_pin2, m4_enable)
    
    
while True:
    print("Before motor forward")
    dc_motor1.one(100)
    dc_motor2.one(100)
    dc_motor3.two(100)
    dc_motor4.two(100)
    print("After motor forward")
    sleep(10)  # Sleep for 1 second (adjust as needed)
    dc_motor1.stop()  # Stop the motors
    dc_motor2.stop()
    dc_motor3.stop()
    dc_motor4.stop()
    sleep(1)  # Sleep for 1 second
    print("Before motor backward")
    dc_motor1.two(100)  # motor is running backward
    dc_motor2.two(100)
    dc_motor3.one(100)
    dc_motor4.one(100)
    print("After motor backward")
    sleep(1)  # Sleep for 1 second
    dc_motor1.stop()  # Stop the motors
    dc_motor2.stop()
    dc_motor3.stop()
    dc_motor4.stop()
    sleep(1)

