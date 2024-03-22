from machine import ADC, Pin
import time

class Joystick:
    def __init__(self, x_pin, y_pin):
        self.x_pin = ADC(Pin(x_pin))
        self.y_pin = ADC(Pin(y_pin))
        self.x_pin.atten(ADC.ATTN_11DB)
        self.y_pin.atten(ADC.ATTN_11DB)
        # self.threshold_x_low = 1000 
        # self.threshold_x_high = 3000
        # self.threshold_y_low = 1000 
        # self.threshold_y_high = 3000
        
    def read_position(self):
        # x_value = self.x_pin.read()
        # y_value = self.y_pin.read()

        # if y_value < self.threshold_y_low:
        #     y_zone = "Mouvement à gauche"
        # elif y_value > self.threshold_y_high:
        #     y_zone = "Mouvement à droite"
        # else:
        #     y_zone = "Position centrale"

        # if x_value < self.threshold_x_low:
        #     x_zone = "Mouvement à gauche"
        # elif x_value > self.threshold_x_high:
        #     x_zone = "Mouvement à droite"
        # else:
        #     x_zone = "Position centrale"

        # return x_value, y_value
        x_value = self.x_pin.read()
        y_value = self.y_pin.read()
        x_value = self.x_pin.read()
        y_value = self.y_pin.read()
        return x_value, y_value


joystick = Joystick(x_pin=35, y_pin=34)

# Boucle principale
while True:
    x, y = joystick.read_position()
    print("X:", x, "Y:", y * -1)
    time.sleep(0.1)
