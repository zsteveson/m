from json import dumps
from block import randString
from block import encodeECB
from block import decodeECB
from urllib.parse import parse_qs
from binascii import hexlify

key = randString(16)

def parse(querystring):
	obj = {}
	pairs = querystring.split('&')
	for pair in pairs:
		key,value = pair.split('=')
		obj[key] = value
	return obj

def profile_for(email):
	return 'email={0}&uid=10&role=user'.format(email.strip('=&'))

def encryptedProfile(email):
	return encodeECB(profile_for(email),key)



def main():

	qstring = 'foo=bar&baz=qux&zap=zazzle'
	dic = { 'foo': 'bar', 'baz': 'qux', 'zap': 'zazzle'}
	assert parse(qstring) == dic
	assert profile_for('zsteveson@gmail.com') == 'email=zsteveson@gmail.com&uid=10&role=user'
	print(hexlify(encryptedProfile('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')))
	#print(encryptedProfile('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'))
	print(hexlify(encryptedProfile('aaaaaaaaaaaaaaaa')))
	print(hexlify(encryptedProfile('')))
main()