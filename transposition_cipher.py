def transposition_cipher(text, key):
  result = ""
  for i in range(key):
    for j in range(len(text) // key):
      result += text[key * j + i]
    
  return result

print(transposition_cipher("hello crypto", 4))


def solve(text, key):
  result = ""
  for i in range(len(text) // key ):
    for j in range(key):
      if(len(text)//key * i + j < len(text)):
        result += text[len(text)//key * j + i ]
    
  return result

print(solve("hoye plctlro", 4))
