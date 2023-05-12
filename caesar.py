
def ceaser(text, shift):
  result = ""
  for i in range(len(text)):
    char = text[i]
    if (char.isupper()): #chr() int to unicode
      result += chr((ord(char) + shift - 65) % 26 + 65)
    else:
      result += chr((ord(char) + shift - 97) % 26 + 97)
  return result

print(ceaser("hello cryptography", 3))
