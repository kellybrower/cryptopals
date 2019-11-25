#to convert a hex string into bytes, use bytearray.fromhex('hexstring')
#byte array is mutable

#example
import base64
print('Converting hex string to raw bytes. Here\'s what they look like:')
dad = bytearray.fromhex('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
print(dad)
print('Now decoded:')
print(dad.decode())

print('Now converting to base64')
mom = base64.b64encode(dad)
print(mom)
print('And decoded')
print(mom.decode())