import keyboard as keyboard
import sounddevice as sd
import numpy as np

recibido = []

def print_sound(indata, outdata, frames, time, status):
    # Apply FFT to the input audio data
    frequencies = np.fft.fft(indata)

    # Find the dominant frequency
    dominant_frequency = np.abs(frequencies).argmax()

    # Perform FSK demodulation based on the dominant frequency
    if dominant_frequency > 1500:
        recibido.append(1)
    elif dominant_frequency < 1000:
        recibido.append(0)

    # Print the dominant frequency
    print("Dominant Frequency:", dominant_frequency)



stream = sd.Stream(callback=print_sound, samplerate=44100)
stream.start()

# Wait for user input to stop the program
input("Press Enter to stop...")

# Stop the audio stream and exit the program
stream.stop()

