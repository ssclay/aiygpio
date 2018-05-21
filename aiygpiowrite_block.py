from nio.block.base import Block
from nio.properties import VersionProperty, BoolProperty
from aiy.pins import PIN_A
from gpiozero import LED


class Aiygpiowrite(Block):

    version = VersionProperty('0.1.0')
    value = BoolProperty(title='Pin State', default='{{$value}}')

    def start(self):
        super().start()
        self.pin = LED(PIN_A)

    def process_signals(self, signals):
        for signal in signals:
            self.pin(self.value(signal))
        self.notify_signals(signals)
