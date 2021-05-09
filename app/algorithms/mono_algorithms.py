code = {
'a': 0,
'b': 1,
'c': 2,
'd': 3,
'e': 4,
'f': 5,
'g': 6,
'h': 7,
'i': 8,
'j': 9,
'k': 10,
'l': 11,
'm': 12,
'n': 13,
'o': 14,
'p': 15,
'q': 16,
'r': 17,
's': 18,
't': 19,
'u': 20,
'v': 21,
'w': 22,
'x': 23,
'y': 24,
'z': 25,
}
key_list = list(code.keys())
val_list = list(code.values())

#Monoalphabetic encryption using substitution
def encrypt_mono(text,key):
  enc = ''
  for x in text:
    if x != ' ':
      val = (code[x] + key)%26
      position = val_list.index(val)
      val = key_list[position]
    else:
      val = ' '
    enc = enc + val
  
  return enc

#Monoalphabetic decryption
def decrypt_mono(text,k):
  dec = ''
  for x in text:
    if x != ' ':
      val = (code[x] - k)%26
      position = val_list.index(val)
      val = key_list[position]
    else:
      val = ' '
    dec = dec + val
  
  return dec