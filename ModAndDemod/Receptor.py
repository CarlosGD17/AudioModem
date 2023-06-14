import sounddevice as sd
import numpy as np
import time as t

recibido = []

def print_sound(indata, outdata, frames, time, status):
    # calcula la longitud del vector
    volume_norm = np.linalg.norm(indata)

    print(volume_norm)
    volume_norm = volume_norm * 10

    print("|" * int(volume_norm))
    if 38 < volume_norm < 45:
        print(f"\n---Recibido: 1---\n")
        recibido.append(1)
        t.sleep(0.1)
    if 15 < volume_norm < 20:
        print(f"\n---Recibido: 0---\n")
        recibido.append(0)
        t.sleep(0.1)



stream = sd.Stream(callback=print_sound, samplerate=44100)
stream.start()

# Wait for user input to stop the program
input("Press Enter to stop...\n")

# Stop the audio stream and exit the program
stream.stop()

print(f"\n---Recibido: {recibido}---")
