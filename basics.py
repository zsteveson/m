from binascii import hexlify
from binascii import unhexlify
from hamming import hamming
from letters import suitability

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

def detectECB(oracle):
	x = set([oracle[i:i+16] for i in range(0, len(oracle), 16)])
	return len(x) != len(oracle) / 16
