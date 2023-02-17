import struct

x = b"computer"

print("8 8-bit integers:", struct.unpack("BBBBBBBB", x))
print("4 unsigned 16-bit integers:", struct.unpack("HHHH", x))
print("2 unsigned 32-bit integers:", struct.unpack("II", x))
print("1 unsigned 64-bit integer:", struct.unpack("Q", x))
print("a 64-bit pointer:", hex(struct.unpack("P", x)[0]))
print("6 ascii characters + 1 signed 16-bit integer:", struct.unpack("6sH", x))
print("2 32-bit floats:", struct.unpack("ff", x))
print("1 64-bit float:", struct.unpack("d", x))
print("2 RGB colors:", struct.unpack("BBBBBBBB", x))

s1={1,2,3,4,5,6}
s2={6,7,8,9}
print(s1&s2)

