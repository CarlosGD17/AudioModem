import sounddevice as sd
import numpy as np
import time as t
import matplotlib.pyplot as plt

recibido = []
data = []
recibiendo = False

def print_sound(indata, outdata, frames, time, status):
    # calcula la longitud del vector
    volume_norm = np.linalg.norm(indata)
    global recibiendo
    volume_norm = volume_norm * 10
    print(volume_norm)
    print("|" * int(volume_norm))
    if volume_norm > 2:
        data.append(volume_norm)
        recibiendo = True
    if recibiendo and volume_norm < 2:
        stream.stop()


stream = sd.Stream(callback=print_sound, samplerate=44100)
stream.start()

# Wait for user input to stop the program
#input("Press Enter to stop...\n")

# Stop the audio stream and exit the program
#stream.stop()

print(f"\n---Recibido: {recibido}---")
plt.plot(data)
plt.show()
