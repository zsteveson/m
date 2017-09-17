from matasano import *
from hamming import hamming
from binascii import hexlify
from binascii import unhexlify

#Exercise 1 
cc = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
assert(hexToBase64(cc) == bytes('SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t','utf-8'))

#Exercise 2 
aa = '1c0111001f010100061a024b53535009181c'
bb = '686974207468652062756c6c277320657965'
assert(hexlify(xor(aa,bb)) == bytes('746865206b696420646f6e277420706c6179','utf-8'))

#Exercise 3 
dd = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
assert(dec(dd)[0] == b"Cooking MC's like a pound of bacon")

#Exercise 4 
f = open('4.txt','r')
for line in f.read().splitlines():
	x = dec(line)
	if (x != []):
		four = x[0]
assert(four == b'Now that the party is jumping\n')

#Exercise 5
ee = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
assert(hexlify(xor(hexFromString(ee),hexFromString("ICE"))) == b'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f')

#Exercise 6 
q = 'this is a test'
z = 'wokka wokka!!!'
assert(hamming(q,z) == 37)
