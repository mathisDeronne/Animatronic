from machine import ADC, Pin
import time

class Joystick:
    def __init__(self, x_pin, y_pin):
        self.x_pin = ADC(Pin(x_pin))
        self.y_pin = ADC(Pin(y_pin))
        self.x_pin.atten(ADC.ATTN_11DB)
        self.y_pin.atten(ADC.ATTN_11DB)

    def read_position(self):
        x_value = self.x_pin.read()
        y_value = self.y_pin.read()
        return x_value, y_value

# Utilisation dans un autre fichier :
# from joystick import Joystick

# Instancier un objet Joystick avec les broches GPIO appropriées
joystick = Joystick(x_pin=2, y_pin=4)

# Boucle principale
while True:
    x, y = joystick.read_position()
    print("X:", x, "Y:", y)
    time.sleep(0.1)
