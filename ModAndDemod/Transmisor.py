import pyaudio
import numpy as np
import time
import matplotlib.pyplot as plt
import random


class Baudio:
    def __init__(self, frequency=440.0, volume=0.5, sampling_rate=44100, duration=0.3):
        # Hz, must be integer
        self.sampling_rate = sampling_rate
        # in senconds
        self.duration = duration
        # since frequency, Hz
        self.frequency = frequency
        # volume range: [0.0 - 1.0]
        self.volume = volume

    def transmit(self):
        p = pyaudio.PyAudio()
        # hace la magia
        samples = (np.sin(
            2 * np.pi * np.arange(self.sampling_rate * self.duration) * self.frequency / self.sampling_rate)).astype(
            np.float32)

        # per @yahweh comment explicitly convert to bytes sequence
        output_bytes = (self.volume * samples).tobytes()

        # for paFloat32 sample values must be in range [-1.0, 1.0]
        stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=self.sampling_rate,
                        output=True)

        # play. May repeat with different volume values (if done interactively)
        start_time = time.time()
        stream.write(output_bytes)
        print("Played sound for {:.2f} seconds".format(time.time() - start_time))

        stream.stop_stream()
        stream.close()

        p.terminate()


class Transmision:
    def __init__(self):
        self.t = Baudio(frequency=600.0)
        self.r = Baudio(frequency=200.0)

    def modular(self, msg):
        print(f"transmitiendo: [{msg}]")
        data = [random.choice([0, 1]) for _ in range(10)]
        for i in data:
            if i == 0:
                self.t.transmit()
            else:
                self.r.transmit()
