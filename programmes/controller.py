from machine import Pin, ADC
import machine

class Joystick(object):
    _x_center = 1789.0
    _y_center = 1817.0
    _pos_x = 4095.0 - _x_center
    _pos_y = 4095.0 - _y_center

    def __init__(self, x_pin, y_pin):
        self._jx = ADC(Pin(x_pin))
        self._jy = ADC(Pin(y_pin))
        
        self._jx.width(machine.ADC.WIDTH_12BIT)
        self._jy.width(machine.ADC.WIDTH_12BIT)
        self._jx.atten(machine.ADC.ATTN_11DB)
        self._jy.atten(machine.ADC.ATTN_11DB)
        
        self._x = 0.0
        self._y = 0.0
        
        self._index = 0
        self._xA = [0, 0, 0]
        self._yA = [0, 0, 0]

    @property
    def x(self):
        '''Return value from -1.0 to 1.0.'''
        return self._x

    @property
    def y(self):
        '''Return value from -1.0 to 1.0.'''
        return self._y

    def update(self):
        self._xA[self._index] = self._jx.read()
        self._yA[self._index] = self._jy.read()

        self._index += 1
        if self._index >= 3:
            self._index = 0

        rx = float(sum(self._xA)) / 3.0 - Joystick._x_center
        ry = float(sum(self._yA)) / 3.0 - Joystick._y_center
        dx = Joystick._pos_x if rx >= 0 else Joystick._x_center
        dy = Joystick._pos_y if ry >= 0 else Joystick._y_center
        self._x = rx / dx
        self._y = ry / dy

        # Value is 1 when not pressed and 0 when pressed.
        

# Usage example:
joystick = Joystick(35, 34)  # Adjust pin numbers as per your wiring

while True:
    joystick.update()
    print("X:", joystick.x, "Y:", joystick.y)
    machine.sleep(200)  # Adjust sleep time as needed
