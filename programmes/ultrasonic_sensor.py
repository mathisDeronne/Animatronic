from machine import Pin, time_pulse_us
import time

class UltraSens:
    def __init__(self, trig_pin, echo_pin, sound_speed=340, trig_pulse_duration_us=10):
        self.trig_pin = Pin(trig_pin, Pin.OUT)
        self.echo_pin = Pin(echo_pin, Pin.IN)
        self.sound_speed = sound_speed
        self.trig_pulse_duration_us = trig_pulse_duration_us

    def measure_distance(self):
        self.trig_pin.value(0)
        time.sleep_us(5)
        self.trig_pin.value(1)
        time.sleep_us(self.trig_pulse_duration_us)
        self.trig_pin.value(0)

        ultrason_duration = time_pulse_us(self.echo_pin, 1, 30000)  # Renvoie le temps de propagation de l'onde (en µs)
        distance_cm = (self.sound_speed * ultrason_duration) / 20000 # Renvoie la distance en cm entre le capteur et l'obstacle

        return distance_cm

# Initialize the ultrasonic sensor
US = UltraSens(trig_pin=25, echo_pin=26)

while True:
    # Measure distance
    distance_cm = US.measure_distance()
    print(f"Distance : {distance_cm} cm")
    time.sleep_ms(100)  # Délai réduit à 100 millisecondes
