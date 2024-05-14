from movements import *
from speaker import *
from ultrasonic_sensor import *
from time import *


US = HCSR04(trig_pin=26, echo_pin=27)

i = 0
escape = 0

while i < 10:
    distance_cm = US.distance_cm()
    print(distance_cm)
    if distance_cm > 12 :
        if i < 1 : 
            Forward()
            sleep(0.5)
            Stop()
            i += 1
        if i < 2 :
            Backward()
            sleep(0.5)
            Stop()
            i += 1
        if i < 3 :
            LD()
            sleep(0.5)
            Stop()
            i += 1
        if i < 4 :
            RLD()
            sleep(0.5)
            Stop()
            i += 1
        if i < 5 :
            RC()
            sleep(0.5)
            Stop()
            i += 1
        if i < 6 :
            RCC()
            sleep(0.5)
            Stop()
            i += 1
        if i < 7 :
            RS()
            sleep(0.5)
            Stop()
            i += 1
        if i < 8 :
            LS()
            sleep(0.5)
            Stop()
            i += 1
        if i < 9 :
            RD()
            sleep(0.5)
            Stop()
            i += 1
        if i < 10 :
            RRD()
            sleep(0.5)
            Stop()
            i += 1
    else :
        if escape < 0 :
            RC()
            sleep(0.5)
            Stop()
            escape += 1
        elif escape < 1 :
            RC()
            sleep(0.5)
            Stop()
            escape += 1
        elif escape < 2 :
            RC()
            sleep(0.5)
            Stop()
            escape += 1
        elif escape < 3 :
            RC()
            sleep(0.5)
            Stop()
            escape += 1
        else :
            i = 10
        