pad_this_1 = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = b"ICE"

def bxor(b1, b2): #use xor for bytes
	result = bytearray()
	for b1, b2 in zip(b1, b2):
		result.append(b1^b2)
	return result

pad_this_1_bytearray = bytearray(pad_this_1)

#to pad 'pad_this_1'
li1 = [k for k in key] * len(pad_this_1)


x = bxor(pad_this_1, li1)
#x = bxor(pad_this_1_bytearray, li1) turn out it doesn't have to be bytearray



print(x.hex())
print(x.decode())
#print(y.hex())

success = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
success_bytes= bytearray.fromhex('0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f')


if x.hex() == success:
	print('You da best!')
else:
	print('You wrong')
undo = bxor(x, li1)
unsuccess = bxor(success_bytes,li1)
print(undo.decode())
print(unsuccess.decode())