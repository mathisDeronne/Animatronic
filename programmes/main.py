from movements import *
from speaker import *
from ultrasonic_sensor import *
from time import *


US = UltraSens(trig_pin=25, echo_pin=26)

i = 0
escape = 0

while i < 10:
    distance_cm = US.measure_distance()
    if distance_cm > 3 :
        if i < 1 : 
            Forward()
            Stop()
            i += 1
        if i < 2 :
            Backward()
            Stop()
            i += 1
        if i < 3 :
            LD()
            Stop()
            i += 1
        if i < 4 :
            RD()
            Stop()
            i += 1
        if i < 5 :
            RC()
            Stop()
            i += 1
        if i < 6 :
            RCC()
            Stop()
            i += 1
        if i < 7 :
            RS()
            Stop()
            i += 1
        if i < 8 :
            LS()
            Stop()
            i += 1
        if i < 9 :
            RRD()
            Stop()
            i += 1
        if i < 10 :
            RLD()
            Stop()
            i += 1
    else :
        if escape < 0 :
            RC()
            Stop()
            escape += 1
        elif escape < 1 :
            RC()
            Stop()
            escape += 1
        elif escape < 2 :
            RC()
            Stop()
            escape += 1
        elif escape < 3 :
            RC()
            Stop()
            escape += 1
        else :
            i = 10
        