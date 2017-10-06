'''
Challenge 3: Single-byte XOR cipher

The hex encoded string:
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

... has been XOR'd against a single character. Find the key, decrypt the message. 

You can do this by hand. But don't: write code to do it for you. 

How? Devise some method for "scoring" a piece of English plaintext.
Character frequency is a good metric. Evaluate each output and choose the one with the best score.  
'''
import binascii
from math import *

# Character frequency
p_i = [0]*256
p_i[32] = .15 # space character
p_i[97] = .082
p_i[98] = .015
p_i[99] = .028
p_i[100] = .042
p_i[101] = .127
p_i[102] = .022
p_i[103] = .020
p_i[104] = .061
p_i[105] = .070
p_i[106] = .001
p_i[107] = .008
p_i[108] = .04
p_i[109] = .024
p_i[110] = .067
p_i[111] = .075
p_i[112] = .019
p_i[113] = .001
p_i[114] = .060
p_i[115] = .063
p_i[116] = .09
p_i[117] = .028
p_i[118] = .01
p_i[119] = .024
p_i[120] = .02
p_i[121] = .001
p_i[122] = .001

# Calculate I_j using the common character frequences and the recorded frequences
def compute_i_j(potential_key, frequencies):
	sum = 0
	for l in range(0, 256):
		sum += p_i[l]*frequencies[(potential_key^l)%256]
	return sum

# Compute frequencies of each letter in the encoded string
def compute_frequencies(c):
	occurrences = [0]*256
	# for letter in c.lower():
	for letter in c:
		occurrences[ord(letter)] += 1
	return occurrences

def breakSingleByteXOR(s):
	frequencies = compute_frequencies(s)

	# compute I_j for all possible shifts
	i_j = [0]*256
	for potential_key in range(0, 256):
		i_j[potential_key] = compute_i_j(potential_key, frequencies)

	max_i_j = max(i_j)
	key = i_j.index(max_i_j)

	l = len(s)
	result = bytearray(l)
	for i in range(l):
		result[i] = ord(s[i]) ^ key
	return [result.decode('utf-8'), max_i_j, chr(key)]

def main():
	encoded = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
	print "Decoded message: ", breakSingleByteXOR(binascii.unhexlify(encoded))[0]

if __name__ == '__main__':
	main()