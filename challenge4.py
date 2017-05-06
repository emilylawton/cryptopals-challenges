'''
Challenge 4: Detect single-character XOR

One of the 60-character strings in this file has been encrypted by single-character XOR. 

Find it.

'''
from challenge3 import breakSingleByteXOR
import binascii

def detect_single_char_XOR(file):
	f = open(file, 'r')
	i_j = []
	messages = []

	for line in f:
		s = binascii.unhexlify(line.strip())

		try:
			result = breakSingleByteXOR(s)
			messages.append(result[0])
			i_j.append(result[1])
		except:
			continue;

	i = i_j.index(max(i_j))
	return messages[i]

def main():
	file = 'text_challenge4.txt'
	result = detect_single_char_XOR(file)
	print "Decoded message: ", result

if __name__ == '__main__':
	main()
