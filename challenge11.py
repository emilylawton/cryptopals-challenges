'''
Challenge 11: An ECB/CBC Detection Oracle

Now that you have ECB and CBC working: 

Write a function to generate a random AES key; that's just 16 random bytes.

Write a function that encrypts data under an unknown key --- that is, a function that generates
a random key and encrypts under it. 

The function should look like: 
encryption_oracle(your-input) => [MEANINGLESS JIBBER JABBER]

Under the hood, have the function append 5-10 bytes (count chosen randomly) before
the plaintext and 5-10 bytes after the plaintext. 

Now, have the function choose to encrypt under ECB 1/2 the time, and under CBC the other half
(just use random IVs each time for CBC). Use rand(2) to decide which to use. 

Detect the block cipher mode the function is using each time. You should end up with
a piece of code that, pointed at a black box that might be encrypting ECB or CBC, tells you
which one is happening. 
'''
import random
import numpy as np
import itertools
from challenge8 import detect_aes_in_ecb_score
from challenge9 import pkcsPadding
from Crypto.Cipher import AES

def generate_random_bytes(bytes=16):
	return np.random.bytes(bytes)

# Generates a random key and encrypts under it
def encryption_oracle(plaintext):
	key = generate_random_bytes()
	IV = generate_random_bytes()
	bytes_before = generate_random_bytes(random.randint(5, 10))
	bytes_after = generate_random_bytes(random.randint(5, 10))

	text = str(pkcsPadding(bytes_before + plaintext + bytes_after, 16))

	if (random.randint(0, 1) == 0):
		return AES.new(key, AES.MODE_ECB).encrypt(text), "ECB"
	else:
		return AES.new(key, AES.MODE_CBC, IV).encrypt(text), "CBC"

# Detects whether a black box is encrypted using ECB or CBC  
def detect_cipher_mode(ciphertext):
	if detect_aes_in_ecb_score(ciphertext, 16) > 0:
		return "ECB"
	else:
		return "CBC"

def main():
	input = 'I\'ll come running to tie your shoes'*32

	for _ in itertools.repeat(None, 100):
		ciphertext, encryption_mode = encryption_oracle(input)
		encryption_mode_detected = detect_cipher_mode(ciphertext) 
		assert(encryption_mode_detected == encryption_mode)

if __name__ == '__main__':
	main()