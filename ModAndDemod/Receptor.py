import keyboard as keyboard
import sounddevice as sd
import numpy as np

volume1 = []
volume3 = []
volume6 = []
volume9 = []

def print_sound(indata, outdata, frames, time, status):
    # calcula la longitud del vector
    volume_norm = np.linalg.norm(indata)

    print(volume_norm)
    volume_norm = volume_norm * 10

    print("|" * int(volume_norm))

    volume = int(input("Que volume es?"))
    if volume == 1:
        volume1.append(volume)
    if volume == 3:
        volume3.append(volume)
    if volume == 6:
        volume6.append(volume)
    if volume == 9:
        volume9.append(volume)
    input("--")



stream = sd.Stream(callback=print_sound, samplerate=44100)
input("-")
stream.start()

# Wait for user input to stop the program
#input("Press Enter to stop...")
while True:
    if keyboard.is_pressed('esc'):
        break


# Stop the audio stream and exit the program
stream.stop()

print()
print(f"Promedio volume 1: {sum(volume1)/len(volume1)}")
print(f"Promedio volume 3: {sum(volume3)/len(volume3)}")
print(f"Promedio volume 6: {sum(volume6)/len(volume6)}")
print(f"Promedio volume 9: {sum(volume9)/len(volume9)}")
