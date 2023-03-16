import wave
import struct
import os

n = 0
IF = 0

while n == 0:
    name = input("Введите название файла: ")
    dir = os.path.abspath(os.curdir)
    for root, dirs, files in os.walk(dir):
        if name in files:
            while IF == 0:
                i_frame = input("Введите натуральное число i из диапазона [2..5]: ")
                if int(i_frame) == float(i_frame) and  1 < int(i_frame) < 6:
                    IF += 1
            n += 1
    if n == 0:
        print("Такого файла нет")

sound = wave.open(name, mode="rb")
frame_count = sound.getnframes()
print(frame_count)
data = sound.readframes(frame_count)
params = sound.getparams()
sound.close()

data = struct.unpack("<" + str(frame_count * 2) + "h", data)
new_data = list(data)
del new_data[::int(i_frame)]
new_frame = struct.pack("<" + str(len(new_data)) + "h", *new_data)
soundout = wave.open(name, mode="wb")
soundout.setparams(params)
soundout.writeframes(new_frame)
soundout.close()
