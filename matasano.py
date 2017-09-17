import base64
from binascii import hexlify
from binascii import unhexlify
import enchant

d = enchant.Dict("en_US")


def hexFromString(a):
	return hexlify(bytes(a,'utf-8'))

def hexToBase64(a):
	return base64.b64encode(unhexlify(a))

def xor(a,b):
	x = []
	a = unhexlify(a)
	b = unhexlify(b)
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

