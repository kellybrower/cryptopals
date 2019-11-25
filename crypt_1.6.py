import base64 as b

def bxor(b1, b2): #use xor for bytes
	result = bytearray()
	for b1, b2 in zip(b1, b2):
		result.append(b1^b2)
	return result
li = list()
string = str()
with open('crypt_64.txt') as fin:
	for line in fin:
		li.append(line.rstrip('\n'))



li_bytes = list()
for l in li:
	li_bytes.append(b.b64decode(l))
	
for s in li_bytes:
	string = string + s.decode()

n = 39
blocks = [bytearray(string[i:i+n], 'utf-8') for i in range(0, len(string), n)]

#make a list of byte i for each block (so all first bytes in entry 1, etc.)
blocks_list = list()
for s in blocks:
	s_list = list()
	for i in range(len(s)):
		s_list.append(s[i])
	blocks_list.append(s_list)

blocks_dict = dict()
for d in blocks_list:
	for x in d:
		blocks_dict[x] = d.count(x)

print(blocks_dict)

xor_key = [76] * len(blocks_list)
print(xor_key)
decode_list = list()
for d in blocks_list:
	for i in range(len(blocks_list)):
		decode_list.append(bxor(blocks_list[i], xor_key).decode(errors = 'ignore'))
for i in range(len(decode_list)):
	print(decode_list[i])		


		
def hamon(s1, s2):
	'''take in two bytes and find hammning distance between binaries'''
	z = '1'
	j = 0
	s1_xor_s2 = bxor(s1,s2)
	for k in range(len(s1_xor_s2)):
		for i in bin(s1_xor_s2[k]):
			if z == i:
				j+=1
	return j
'''
s1 = b'this is a test'
s2 = b'wokka wokka!!!'

print(hamon(s1,s2))
'''
KEYSIZES = [i for i in range(2,40)]
errors = list()
for i in KEYSIZES:
	errors.append((hamon(li_bytes[0][:i+1], li_bytes[0][i+1:(i+i+1)]))/i)

#print(errors)

#try keysize 37 and 39(first)