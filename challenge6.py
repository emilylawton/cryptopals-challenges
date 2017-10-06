'''
Challenge 6: Break repeating-key XOR 

There's a file here. It's been base64'd after being encrypted with repeating-key XOR. 

Decrypt it. 

Here's how: 
1. Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40. 

2. Write a function to compute the edit distanct/Hamming distance between two strings.
The Hamming distance is just the number of differing bits. The distance between:
this is a test
and
wokka wokka!!!
is 37. Make sure your code agrees before you proceed. 

3. For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, 
and find the edit distance between them. Normalize this result by dividing by KEYSIZE.

4. The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed with perhaps the 
smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances. 

5. Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.

6. Now transpose the blocks: make a block that is the first byte of every block, and a block that is
the second byte of every block, and so on. 

7. Solve each block as if it was single-character XOR. You already have code to do this.

8. For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR
key byte for that block. Put them together and you have the key. 

'''
from binascii import a2b_base64
from challenge3 import breakSingleByteXOR
from challenge5 import encrypt

def hammingDistance(x, y):
	assert(len(x) == len(y))
	d = 0
	for i in range(len(x)):
		d += bin(ord(x[i])^(ord(y[i]))).count('1')
	return d

def normalized_hamming_distance(data, size):
	s = 0
	num_blocks = 10
	for i in range(0,num_blocks):
		first_bytes = data[(i+0)*size:(i+1)*size]
		second_bytes = data[(i+1)*size:(i+2)*size]
		s += hammingDistance(first_bytes, second_bytes)/float(size)
	return s / float(num_blocks)

def main():
	file = 'data/text_challenge6.txt'
	text = ""
	for line in open(file):
		text += line.strip()
	text = a2b_base64(text)

	smallest_normalized_hamming_distance = float('inf')
	norm_ham = 0
	best_keysize = -1

	min_keysize = 2
	max_keysize = 40
	for keysize in range(min_keysize, max_keysize+1):
		norm_ham = normalized_hamming_distance(text, keysize)
		if norm_ham < smallest_normalized_hamming_distance:
			smallest_normalized_hamming_distance = norm_ham
			best_keysize = keysize

	print "Key size: " + str(best_keysize)
	print

	blocks = [text[i::best_keysize] for i in range(best_keysize)]

	decoded_data = [breakSingleByteXOR(d) for d in blocks]

	key = ''.join(d[2] for d in decoded_data)
	print "Key: " + key
	print

	decoded_data = encrypt(text, key)
	print decoded_data.strip()

if __name__ == '__main__':
	main()