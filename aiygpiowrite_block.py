from enum import Enum
from nio.block.base import Block
from nio.properties import VersionProperty, SelectProperty, Property
from aiy.pins import *
from gpiozero import LED


class PinSelection(Enum):

    PIN_A = PIN_A
    PIN_B = PIN_B
    PIN_C = PIN_C
    PIN_D = PIN_D

class Aiygpiowrite(Block):

    version = VersionProperty('0.1.0')
    value = Property(title='Pin State', default='{{$value}}')
    aiy_pin = SelectProperty(PinSelection,
                             title="Pin Selection",
                             default=PinSelection.PIN_A)

    def start(self):
        super().start()
        self.pin = LED(self.aiy_pin().value)

    def process_signals(self, signals):
        for signal in signals:
            self.pin.value = not self.value(signal)
        self.notify_signals(signals)
