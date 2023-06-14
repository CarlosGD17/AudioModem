import time

import numpy as np

import Transmisor
from matplotlib import pyplot as plt


p = Transmisor.Transmision()
"""
d = [0, 0, 0, 0, 0, 0, 0, 0]
print(len(d))
p.modular(d)

d = [0, 1, 0, 1, 0, 1, 0, 1]
print(len(d))
p.modular(d)

d = [1, 0, 1, 0, 1, 0, 1, 0]
print(len(d))
p.modular(d)

d = [1, 1, 1, 1, 1, 1, 1, 1]
print(len(d))
p.modular(d)


while True:
    volume = int(input("Digite el volumen (1, 3, 6, 9): "))
    p.calibrar(volume)

d = p.codificar("hola", 0)
print(len(d))
"""

p.modular([0, 1, 1, 0, 0, 1, 1, 0, 0])
#time.sleep(1)
#p.modular([1, 1, 1, 1, 1, 1, 1, 1])
"""
with open("D:\Carlos\Desktop\goku_idle.jpg", "rb") as f:
    print("read:", f.read())
    archivo = p.codificar(f, extension=1)
    print(len(archivo))
    p.modular(archivo)


def get_binary_representation(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()

    # Convert binary data to a string of binary digits
    binary_string = ''.join(format(byte, '08b') for byte in binary_data)

    return binary_string


file_path = 'D:\Carlos\Desktop\hola.txt'
binary_representation = get_binary_representation(file_path)
print(binary_representation)


def save_binary_as_file(binary_string, output_file_path):
    # Convert the binary string to bytes
    bytes_data = bytes(int(binary_string[i:i + 8], 2) for i in range(0, len(binary_string), 8))

    # Write the bytes to a new file
    with open(output_file_path, 'wb') as file:
        file.write(bytes_data)
        print("Guardado")


output = 'D:\Carlos\Desktop\hola2.txt'
save_binary_as_file(binary_representation, output)
"""
