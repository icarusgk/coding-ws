encoded = 'HlAdghmcXnt'
key = 256
key_to_bytes = (key).to_bytes(2, 'little')

n = sum(key_to_bytes)

[print(chr(ord(char) + n), end="") for char in encoded]
