binary_text = "1011001 1101111 1110101 1110010 100000 1001101 1100101 1110011 1110011 1100001 1100111 1100101"

normal = "".join(chr(int(c, 2)) for c in binary_text.split(" "))

print(normal)