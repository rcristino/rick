#!/usr/bin/env python3
from ev3dev.ev3 import *

class TouchSensor:

    def __init__(self):
        self.ts = TouchSensor()

    def value(self):
        return self.ts.value()

        