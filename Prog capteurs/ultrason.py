from machine import Pin, time_pulse_us
import time

trig_pin = Pin(5, Pin.OUT)
echo_pin = Pin(18, Pin.IN)

SOUND_SPEED = 340
TRIG_PULSE_DURATION_US = 10

while True:
    # Préparation du signal
    trig_pin.off()
    time.sleep_us(2)
    
    # Création d'une impulsion de 10 µs
    trig_pin.on()
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trig_pin.off()

    # Récupération du temps de propagation de l'onde (en µs)
    ultrason_duration = time_pulse_us(echo_pin, 1, 20000)  # Durée maximale de 20000 µs

    # Calcul de la distance
    distance_cm = ultrason_duration * SOUND_SPEED / 2 * 0.0001

    # Affichage de la distance
    print("Distance (cm):", distance_cm)

    time.sleep(1)