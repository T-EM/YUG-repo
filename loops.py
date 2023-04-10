# for i in range(1, 11, 3):
#     print(i)

# l = ("Tanmay", "Yugandhar", "Raj")
# for s in l:
#     print(s)

from sys import stdout as std
from time import sleep

buffers = ["Tanmay", "Yugandhar"]
buf = ""
temp = ""

while 1:
    std.write("\rHello, ")
    std.flush()
    sleep(.300)
    for s in buffers:
        for n in s:
            buf += n
            std.write(f"\rHello, {buf}")
            std.flush()
            sleep(.300)
        for n in s:
            temp += "\0"
            std.write(f"\rHello, {temp}")
            std.flush()
        for n in s:
            buf[:-1]
            std.write(f"\rHello, {buf}")
            std.flush()
            sleep(.300)
        buf = ""
        temp = " "
    std.flush()

# for i in range(1, 100001):
#     std.write(f"\r{i}. Good Morning!")
#     std.flush()
