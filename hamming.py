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