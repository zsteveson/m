import base64
import binascii 
import enchant

d = enchant.Dict("en_US")

aa = '1c0111001f010100061a024b53535009181c'
bb = '686974207468652062756c6c277320657965'
cc = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
dd = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
ee = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

def binFromHex(a):
	return binascii.unhexlify(a)

def binToHex(a):
	return binascii.hexlify(a)

def hexFromString(a):
	return binascii.hexlify(bytes(a,'utf-8'))

def hexToBase64(a):
	return base64.b64encode(binFromHex(a))

def xor(a,b):
	x = []
	a = binFromHex(a)
	b = binFromHex(b)
	for idx,byte in enumerate(a):
		x.append(byte ^ b[idx % len(b)])
	return bytes(x)

def trials(a):
	x = []
	for i in '0123456789abcdef':
		for j in '0123456789abcdef':
			x.append(xor(a,i+j))
	return x

def check(string):
	words = str(string).split()
	for word in words:
		if (len(word) > 2 and d.check(word) == True):
			return True
	return False

def dec(line):
	return [trial for trial in trials(line) if check(trial)]

def exercise4():
	f = open('4.txt','r')
	for line in f.read().splitlines():
		x = dec(line)
		if (x != []):
			return x

def hamming(a,b):
	a = bytes(a,'utf-8')
	b = bytes(b,'utf-8')
	return compare(a,b)

def compare(a,b):
	count = 0
	for idx,byte in enumerate(a):
		count += compareBits(byte,b[idx])
	return count

def compareBits(a,b):
	a = format(a, '#010b')
	b = format(b, '#010b')
	count = 0
	for idx, bit in enumerate(a):
		if(bit != b[idx]):
			count += 1
	return count



#Exercise 1 
assert(hexToBase64(cc) == bytes('SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t','utf-8'))

#Exercise 2 
assert(binascii.hexlify(xor(aa,bb)) == bytes('746865206b696420646f6e277420706c6179','utf-8'))

#Exercise 3 
assert(dec(dd)[0] == b"Cooking MC's like a pound of bacon")

#Exercise 4 
#assert(exercise4()[0] == b'Now that the party is jumping\n')

#print(binascii.hexlify(xor(hexFromString(ee),hexFromString("ICE"))))

q = 'this is a test'
z = 'wokka wokka!!!'

print(hamming(q,z))

