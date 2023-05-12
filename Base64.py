import base64

text = "Hello World"
byte_string = text.encode()
encode = base64.b64encode(byte_string)
print(encode.decode())

decode = base64.b64decode(encode)
print(decode.decode())