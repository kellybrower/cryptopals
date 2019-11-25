print('Now we want to practice XOR\'ing')
print(' We will XOR the hex string "1c0111001f010100061a024b53535009181c" \n')
print('with the hex string "686974207468652062756c6c277320657965"')
byte1 = bytearray.fromhex('1c0111001f010100061a024b53535009181c')
byte2 = bytearray.fromhex('686974207468652062756c6c277320657965')
def bxor(b1, b2): #use xor for bytes
	result = bytearray()
	for b1, b2 in zip(b1, b2):
		result.append(b1^b2)
	return result
print('and here\'s the byte string resulting from \n')
print('byte strings XOR\'d one bit at a time')
x = bxor(byte1,byte2)
print(x)
print('and here\'s the value decoded')
print(x.decode())

print('but the goal of this exercise was to return the val')
print(x.hex())

