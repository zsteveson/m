from binascii import hexlify
from binascii import unhexlify
from hamming import hamming
from letters import suitability
from crypto.Cipher import AES
import string
import random
import base64

def hexToBase64(a):
	return base64.b64encode(unhexlify(a))

def xor(a,b):
	x = []
	for idx,byte in enumerate(a):
		x.append(byte ^ b[idx % len(b)])
	return bytes(x)

def trials(a):
	x = []
	for i in range(0,128):
		byte = (i).to_bytes(1,byteorder='big')
		xxx = xor(a,byte)
		x.append({'key' : byte,'xor':xxx})
	return x


def sortBySuitability(trials):
	for trial in trials:
		trial['suitability'] = suitability(trial.get('xor'))
	return sorted(trials, key=lambda trial: trial.get('suitability'))

def block(b,length):
	transposed = [b''] * length
	for i in range(0,len(b),2):
		transposed[int(i / 2) % length] += b[i:i+2]
	return transposed
			
def pad(block,length):
	block = bytes(block,'utf-8')
	block += b'\x04'*(length - len(block))
	return block

def encodeECB(text, key):
	aes = AES.new(key, AES.MODE_ECB)
	if (len(text) % 16 != 0):
		text = pad(text,len(text)+len(text) % 16)
	return aes.encrypt(text)

def decodeECB(text, key):
	aes = AES.new(key, AES.MODE_ECB)
	return aes.decrypt(text)

def encodeCBC(text,key,iv):
	lastblock = iv
	blocks = [text[i:i+16] for i in range(0, len(text), 16)]
	eblocks = []
	for block in blocks:
		if (len(block) < 16):
			block = pad(block,16)
		lastblock = encodeECB(bxor(block,lastblock),key)
		eblocks.append(lastblock)
	return b''.join(eblocks)

def decodeCBC(text,key,iv):
	lastblock = iv
	blocks = [text[i:i+16] for i in range(0, len(text), 16)]
	dblocks = []
	for block in blocks:
		dblocks.append(bxor(decodeECB(block,key),lastblock))
		lastblock = block
	return b''.join(dblocks)

def ten():
	ten = open('10.txt')
	ff = base64.b64decode(ten.read())
	print(decodeCBC(ff,'YELLOW SUBMARINE',b'\x00' * 16))

def randString(n):
	return ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))

