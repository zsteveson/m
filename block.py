from crypto.Cipher import AES
from basics import xor
from basics import detectECB
from random import randint
from random import choices
from base64 import b64decode
import string
from binascii import hexlify
from hamming import findLowestHammingLength

def pad(block,length):
	if(type(block) == str):
		block = bytes(block,'utf-8')
	block += b'\x04'*(length - len(block))
	return block

def encodeECB(text, key):
	aes = AES.new(key, AES.MODE_ECB)
	if (len(text) % 16 != 0):
		text = pad(text,len(text)+ 16 - len(text) % 16)
	return aes.encrypt(text)

def decodeECB(text, key):
	aes = AES.new(key, AES.MODE_ECB)
	return aes.decrypt(text)

def encodeCBC(text,key,iv):
	lastblock = bytes(iv,'utf-8')
	blocks = [text[i:i+16] for i in range(0, len(text), 16)]
	eblocks = []
	for block in blocks:
		if (len(block) < 16):
			block = pad(block,16)
		else:
			block = bytes(block,'utf-8')
		lastblock = encodeECB(xor(block,lastblock),key)
		eblocks.append(lastblock)
	return b''.join(eblocks)

def decodeCBC(text,key,iv):
	lastblock = iv
	blocks = [text[i:i+16] for i in range(0, len(text), 16)]
	dblocks = []
	for block in blocks:
		dblocks.append(xor(decodeECB(block,key),lastblock))
		lastblock = block
	return b''.join(dblocks)

def randString(n):
	return ''.join(choices(string.ascii_uppercase + string.digits, k=n))


def encryption_oracle(text):
	b = randString(randint(5,10)) + text + randString(randint(5,10))
	key = randString(16)
	iv = randString(16)
	if (randint(0,1) == 0):
		return ['ECB', encodeECB(b,key)]
	else:
		return ['CBC',encodeCBC(b,key,iv)]

key = randString(16)
iv = randString(16)
t = b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')

def oracle(text,t):
	return encodeECB(text + t,key)

def findLength():
	string = ''
	while (True):
		encoded = oracle(string)
		if (detectECB(encoded)):
			break
		else:
			string += 'a'
	return len(string)/2

def allBytes():
	b = []
	for i in range(0,128):
		b.append((i).to_bytes(1,byteorder='big').decode("utf-8"))
	return b

def paddingDecryption(ciphertext):
	plaintext = ''
	padding = bytes('A' * 52,'utf-8')
	blocksize = findLowestHammingLength(oracle(padding, ciphertext))
	for blockIndex in range(0, len(ciphertext) % blocksize - 1):
		for i in reversed(range(0, blocksize)):
			guessToCharacter = {}
			for character in allBytes():
				guess = oracle(bytes('A' * i + plaintext + character, 'utf-8'), ciphertext)[:blocksize * (blockIndex+1)]
				guessToCharacter[guess] = character
			trial = oracle(bytes('A' * i,'utf-8'), ciphertext)[: blocksize * (blockIndex + 1)]
			plaintext += guessToCharacter[trial]
	return plaintext

print(paddingDecryption(t))




