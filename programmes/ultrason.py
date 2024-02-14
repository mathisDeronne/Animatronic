from machine import Pin, time_pulse_us
import time

TRIG_PIN = 27
ECHO_PIN = 14
SOUND_SPEED = 340  # Vitesse du son dans l'air
TRIG_PULSE_DURATION_US = 10

trig_pin = Pin(TRIG_PIN, Pin.OUT)
echo_pin = Pin(ECHO_PIN, Pin.IN)

while True:
    # Prépare le signal
    trig_pin.value(0)
    time.sleep_us(5)
    # Crée une impulsion de 10 µs
    trig_pin.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trig_pin.value(0)

    ultrason_duration = time_pulse_us(echo_pin, 1, 30000)  # Renvoie le temps de propagation de l'onde (en µs)
    distance_mm = (SOUND_SPEED * ultrason_duration) / 20000

    print(f"Distance : {distance_mm} mm")
    time.sleep_ms(100)  # Délai réduit à 100 millisecondes