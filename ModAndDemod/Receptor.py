import sounddevice as sd
import numpy as np


def print_sound(indata, outdata, frames, time, status):
    # calcula la longitud del vector
    volume_norm = np.linalg.norm(indata)

    print(volume_norm)
    volume_norm = volume_norm * 10

    print("|" * int(volume_norm))


with sd.Stream(callback=print_sound, samplerate=44100):
    sd.sleep(10000)
