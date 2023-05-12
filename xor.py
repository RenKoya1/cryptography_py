import base64
from itertools import cycle

def xor_encode(text, key='awesomepassword'):
  xored = ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(text, cycle(key)))
  xored = base64.b64encode(xored.encode()).decode()
  return xored

def xor_decode(text, key='awesomepassword'):
    text = base64.b64decode(text).decode()  # バイト列を文字列に変換
    xored = ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(text, cycle(key)))
    return xored

secret_text = "XOR procedure"

encoded = xor_encode(secret_text)
print(encoded)
print(xor_decode(encoded))

