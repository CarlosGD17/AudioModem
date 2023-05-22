class Transmisor:
    def __init__(self):
        self.bit_rate = 1000
        self.frequency = 1500
        self.volume = 2000

    def transmit(self, msg):
        # hace la magia
        print(msg)
