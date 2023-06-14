import sounddevice as sd
import numpy as np

recibido = []

def print_sound(indata, outdata, frames, time, status):
    # calcula la longitud del vector
    volume_norm = np.linalg.norm(indata)

    print(volume_norm)
    volume_norm = volume_norm * 10

    print("|" * int(volume_norm))
    if volume_norm > 38 and volume_norm < 45:
        recibido.append(1)



stream = sd.Stream(callback=print_sound, samplerate=44000)
stream.start()

# Wait for user input to stop the program
input("Press Enter to stop...\n")

# Stop the audio stream and exit the program
stream.stop()
