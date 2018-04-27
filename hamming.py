from math import floor

def hamming(a,b):
	if(type(a) == str):
		a = bytes(a,'utf-8')
	if(type(b) == str):
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

def findLowestHammingLength(xx):
	lowestLength = 2
	lowestHamming = compareIntervalHamming(xx,2)
	for i in range(3,37):
		intervalHamming = compareIntervalHamming(xx,i)
		if(intervalHamming < lowestHamming):
			lowestHamming = intervalHamming
			lowestLength = i
	return lowestLength

def compareIntervalHamming(xx,n):
	score = 0
	k = int(150 / n)
	for i in range(0,k):
		score += hamming(xx[n*i:n*(i+1)],xx[n*(i+1):n*(i+2)]) / n
	return score / k
