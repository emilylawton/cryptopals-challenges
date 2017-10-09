'''
Challenge 8: Detect AES in ECB mode

In this file are a bunch of hex-encoded ciphertexts. 

One of them has been encrypted with ECB.

Detect it. 

Remember that the problem wiht ECB is that it is stateless and deterministic;
the same 16 byte plaintext block will always produce the same 16 byte ciphertext.
'''

import itertools

def detect_aes_in_ecb_score(x, k):
	chunks = [x[i:i+k] for i in range(0, len(x), k)]
	pairs = itertools.combinations(chunks, 2)
	matches = 0
	for p in pairs:
		matches += (p[0] == p[1])
	return matches

def main():
	file = 'data/text_challenge8.txt'
	text = []
	for line in open(file):
		text.append(line.strip())

	lineCount = 1
	for line in text:
		if detect_aes_in_ecb_score(line, 16) > 0:
			print "Line " + str(lineCount) + " has likely been encrypted with AES in ECB mode."
			print
			print line
			print
		lineCount += 1

if __name__ == '__main__':
	main()
