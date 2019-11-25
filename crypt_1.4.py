def bxor(b1, b2): #use xor for bytes
	result = bytearray()
	for b1, b2 in zip(b1, b2):
		result.append(b1^b2)
	return result

li = list()
with open('crypt.txt') as fin:
	for line in fin:
		li.append(line.rstrip('\n'))


dad = list()
for l in li:
	dad.append(bytearray.fromhex(l))

dad_dict = dict()
for d in dad:
	for x in d:
		dad_dict[d.count(x)] = x
y = dad_dict[max(dad_dict)]
linda = [dad_dict[max(dad_dict)]] * len(dad)
for d in dad:
	print(bxor(d, linda).decode(errors = 'ignore'))
		
# note: i had to jerry-rig it, and i got lucky. once I saw:
		
#bytearray(b'nOWÑx00THATÑx00THEÑx00PARTYÑx00ISÑx00JUMPING*')

#then I saw:
#bytearray(b'nOW\x00THAT\x00THE\x00PARTY\x00IS\x00JUMPING*')

		
		
#"nOWTHATTHEPARTYISJUMPING*"