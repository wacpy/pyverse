message = "Your Message"
binary = " ".join(format(ord(c), "b") for c in message)
print(binary)