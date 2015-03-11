############################################################
## Wrapper module for John's 8 leds to be used by chidren ##
##                                                        ##
## Written by Yolanda Robla  -  v0.1                      ##
##            info@ysoft.biz                              ##
############################################################
##
## v0.1 - Initial release                    - 15/08/13
##

import RPIO
import time

class Botluz:
    def __init__(self):
        RPIO.setwarnings(False)
        RPIO.setmode(RPIO.BOARD)
        self.buttons = [10, 11, 12, 13, 15, 16, 18, 22]
        self.leds = [3, 5, 7, 26, 24, 21, 19, 23]

        # shut down leds
        for x in self.leds:
            RPIO.setup(x, RPIO.OUT)
            RPIO.output(x, RPIO.LOW)

        # prepare buttons
        for x in self.buttons:
            RPIO.setup(x, RPIO.IN, pull_up_down=RPIO.PUD_UP)

    def __exit__(self, type, value, traceback):
        RPIO.cleanup()

    def encenderluces(self):
        for x in self.leds:
            RPIO.output(x, RPIO.HIGH)

    def apagarluces(self):
        for x in self.leds:
            RPIO.output(x, RPIO.LOW)

    def encenderluz(self, numero):
        numero = numero - 1
        if numero<0 or numero>7:
            return
        RPIO.output(self.leds[numero], RPIO.HIGH)

    def apagarluz(self, numero):
        numero = numero -1
        if numero<0 or numero>7:
            return
        RPIO.output(self.leds[numero], RPIO.LOW)

    def esperarboton(self, numero):
        numero = numero -1
        if numero<0 or numero>7:
            return

        while True:
            result = RPIO.input(self.buttons[numero])
            if result == False:
                return True
            time.sleep(0.2)

    def esperarbotones(self):
        while True:
            i = 1
            for button in self.buttons:
                result = RPIO.input(button)
                if result == False:
                    return i
                i+=1
            time.sleep(0.2)
