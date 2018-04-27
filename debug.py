from matasano import *
from hamming import hamming
from binascii import hexlify
from binascii import unhexlify

aa = '1c0111001f010100061a024b53535009181c'
bb = '686974207468652062756c6c277320657965'

dd = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
assert(sortBySuitability(trials(dd))[-1] == b"Cooking MC's like a pound of bacon")


x = findLowestHammingLength('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')
print(x)