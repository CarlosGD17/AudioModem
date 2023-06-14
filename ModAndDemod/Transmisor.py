import pyaudio
import numpy as np
import time
import bitarray


class Baudio:
    def __init__(self, frequency=1117.0, volume=0.5, sampling_rate=44100, duration=0.01):
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
        # x = [muestreo * duracion]
        # sin(2*pi*x*frecuencia/muestreo)
        samples = (np.sin(
            2 * np.pi * np.arange(self.sampling_rate * self.duration) * self.frequency / self.sampling_rate)).astype(
            np.float32)

        #plt.plot(self.volume * samples)
        #plt.show()

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
        #print("Played sound for {:.2f} frequency".format(self.frequency))
        print("Played sound for {:.2f} volume".format(self.volume))

        stream.stop_stream()
        stream.close()
        p.terminate()


class Transmision:
    def __init__(self):
        # 4 baudios
        # bit/segundo = log_2_(4) = 2
        #self.b1 = Baudio(frequency=1117.0)
        self.b1 = Baudio(volume=0.1)
        #self.b2 = Baudio(frequency=2117.0)
        self.b2 = Baudio(volume=0.3)
        #self.b3 = Baudio(frequency=3117.0)
        self.b3 = Baudio(volume=0.6)
        #self.b4 = Baudio(frequency=4117.0)
        self.b4 = Baudio(volume=0.9)

    def modular(self, bits):
        print(f"transmitiendo: [{bits}]")
        data = bits
        # data = [random.choice([0, 1]) for _ in range(10)]
        for i in range(0, len(data), 2):
            if data[i] == 0 and data[i+1] == 0:
                self.b1.transmit()
            elif data[i] == 0 and data[i+1] == 1:
                self.b2.transmit()
            elif data[i] == 1 and data[i+1] == 0:
                self.b3.transmit()
            elif data[i] == 1 and data[i+1] == 1:
                self.b4.transmit()

    def codificar(self, msg, nombre):
        # mensaje
        if nombre == 0:
            codificado = bitarray.bitarray()
            codificado.frombytes(msg.encode('utf-8'))
        # archivo
        else:
            codificado = []
            for i in msg:
                for j in range(7, -1, -1):
                    bit = (i >> i) & 1
                    codificado.append(bit)
        print(codificado)
        return codificado

    def calibrar(self, volume):
        if volume == 1:
            self.b1.transmit()
        if volume == 3:
            self.b2.transmit()
        if volume == 6:
            self.b3.transmit()
        if volume == 9:
            self.b4.transmit()

    def contruyeTrama(self, ):
        trama = []
        # inicio de la trama
        trama.append(1)
        trama.append(1)

        # final de la trama
        trama.append(1)
