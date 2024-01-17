from pyb import Pin, Timer
import time
import gc

BP1 = 0
BP2 = 0
BP3 = 1

sw1 = pyb.Pin('SW1')
sw1.init(pyb.Pin.IN, pyb.Pin.PULL_UP, af=-1)
sw2 = pyb.Pin('SW2')
sw2.init(pyb.Pin.IN, pyb.Pin.PULL_UP, af=-1)
sw3 = pyb.Pin('SW3')
sw3.init(pyb.Pin.IN, pyb.Pin.PULL_UP, af=-1)

red_led = pyb.LED(1)
blue_led = pyb.LED(3)
green_led = pyb.LED(2)

motor_pin1 = pyb.Pin('D4', Pin.OUT_PP)
motor_pin2 = pyb.Pin('D5', Pin.OUT_PP)

tim1 = Timer(1, freq=1000)
ch3 = tim1.channel(3, Timer.PWM, pin=motor_enable)

def ITbutton1(line):


global BP1
global BP2
global BP3

BP1 = BP1 + 1
BP2 = 0
BP3 = 0


def ITbutton2(line):


global BP1
global BP2
global BP3


BP1 = 0
BP2 = BP2 + 1
BP3 = 0


def ITbutton3(line):

global BP1
global BP2
global BP3

BP1 = 0
BP2 = 0
BP3 = BP3 + 1


irq_1 = pyb.ExtInt(sw1, pyb.ExtInt.IRQ_FALLING, pyb.Pin.PULL_UP, ITbutton1)
irq_2 = pyb.ExtInt(sw2, pyb.ExtInt.IRQ_FALLING, pyb.Pin.PULL_UP, ITbutton2)
irq_3 = pyb.ExtInt(sw3, pyb.ExtInt.IRQ_FALLING, pyb.Pin.PULL_UP, ITbutton3)


def motor_state(speed):


global BP1
global BP2
global BP3

if((BP1 != 0) and (BP2 == 0) and (BP3 == 0)):
blue_led.on()

ch3.pulse_width_percent(speed)

if((BP1 == 0) and (BP2 != 0) and (BP3 == 0)):
green_led.on()


ch3.pulse_width_percent(speed)

if((BP1 == 0) and (BP2 == 0) and (BP3 != 0)):
red_led.on()

ch3.pulse_width_percent(0)

speed = 100

while True:

blue_led.off()
green_led.off()
red_led.off()


motor_state(speed)

gc.collect()



