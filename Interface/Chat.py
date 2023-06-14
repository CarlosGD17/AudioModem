import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

# Parámetros de configuración
CHUNK = 1024  # Tamaño del búfer de audio
RATE = 44100  # Tasa de muestreo (en Hz)

# Configurar la ventana y el gráfico
plt.ion()  # Modo interactivo
fig, ax = plt.subplots()
x = np.arange(0, CHUNK) * RATE / CHUNK
line, = ax.plot(x, np.zeros(CHUNK))

# Callback para procesar el audio en tiempo real
def audio_callback(indata, frames, time, status):
    # Convertir los datos de audio en un array numpy
    audio_data = indata[:, 0]  # Obtener solo el canal izquierdo (mono)

    # Calcular la Transformada de Fourier
    fft = np.fft.fft(audio_data)
    frequencies = np.fft.fftfreq(len(audio_data), 1/RATE)

    # Obtener las frecuencias positivas
    positive_freq_indices = np.where(frequencies >= 0)
    positive_frequencies = frequencies[positive_freq_indices]
    magnitude = np.abs(fft[positive_freq_indices])

    # Actualizar la visualización del espectro de frecuencias
    line.set_ydata(magnitude)
    ax.relim()
    ax.autoscale_view()

    # Actualizar el gráfico
    fig.canvas.draw()
    fig.canvas.flush_events()

# Configurar la captura de audio en tiempo real
stream = sd.InputStream(callback=audio_callback, channels=1, samplerate=RATE, blocksize=CHUNK)

# Iniciar la captura de audio en tiempo real
stream.start()

# Mantener el programa en ejecución
while True:
    try:
        plt.pause(0.1)
    except KeyboardInterrupt:
        # Detener la captura de audio y cerrar el stream si se presiona Ctrl+C
        stream.stop()
        stream.close()
        break
