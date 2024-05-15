from machine import PWM, Pin
from time import sleep

Mavd1 = Pin(22, Pin.OUT)
Mavd2 = Pin(23, Pin.OUT)
Mavg1 = Pin(19, Pin.OUT)
Mavg2 = Pin(18, Pin.OUT)

Mard1 = Pin(4, Pin.OUT)
Mard2 = Pin(16, Pin.OUT)
Marg1 = Pin(2, Pin.OUT)
Marg2 = Pin(15, Pin.OUT)

def Forward() :
    Mavd1.on()
    Mavd2.off()
    Mavg1.on()
    Mavg2.off()
    
    Mard1.on()
    Mard2.off()
    Marg1.on()
    Marg2.off()


def Backward () :
    Mavd1.off()
    Mavd2.on()
    Mavg1.off()
    Mavg2.on()
    
    Mard1.off()
    Mard2.on()
    Marg1.off()
    Marg2.on()

def LD():
    print("left")
    Mavd1.on()
    Mavd2.off()
    Mavg1.off()
    Mavg2.off()
    
    Mard1.off()
    Mard2.off()
    Marg1.on()
    Marg2.off()
    return

def RD():
    Mavd1.off()
    Mavd2.off()
    Mavg1.on()
    Mavg2.off()
    
    Mard1.on()
    Mard2.off()
    Marg1.off()
    Marg2.off()

def RCC() :
    Mavg1.on()
    Mavg2.off()
    Mavd1.off()
    Mavd2.on()

    
    
    Marg1.on()
    Marg2.off()
    Mard1.off()
    Mard2.on()

def RC() :
    Mavd1.on()
    Mavd2.off()
    Mavg1.off()
    Mavg2.on()
    
    Mard1.on()
    Mard2.off()
    Marg1.off()
    Marg2.on()

def RS() :
    Mavd1.off()
    Mavd2.on()
    Mavg1.on()
    Mavg2.off()
    
    Mard1.on()
    Mard2.off()
    Marg1.off()
    Marg2.on()

def LS() :
    Mavd1.on()
    Mavd2.off()
    Mavg1.off()
    Mavg2.on()
    
    Mard1.off()
    Mard2.on()
    Marg1.on()
    Marg2.off()

def RDD() :
    Mavd1.off()
    Mavd2.off()
    Mavg1.off()
    Mavg2.on()
    
    Mard1.off()
    Mard2.on()
    Marg1.off()
    Marg2.off()

def RLD() :
    Mavd1.off()
    Mavd2.on()
    Mavg1.off()
    Mavg2.off()
    
    Mard1.off()
    Mard2.off()
    Marg1.off()
    Marg2.on()

def Stop() :
    Mavd1.off()
    Mavd2.off()
    Mavg1.off()
    Mavg2.off()
    
    Mard1.off()
    Mard2.off()
    Marg1.off()
    Marg2.off()


