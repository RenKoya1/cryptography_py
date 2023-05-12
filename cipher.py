def cipher(text):
  result = ""
  for i in range(len(text)):
    result  = result + text[len(text) - i - 1] 
  
  return result

print(cipher("hello cryptography"))