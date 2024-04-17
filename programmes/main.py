from movements import *
from speaker import *
from ultrasonic_sensor import *
from time import *


US = UltraSens(trig_pin=25, echo_pin=26)

while True:
    # Measure distance
    distance_cm = US.measure_distance()
    if distance_cm > 10 {
        #////
    }