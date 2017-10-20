'''
Challenge 10: Implement CBC mode

CBC mode is a block cipher mode that allows us to encrypt irregularly-sized
messages, despite the fact that a block cipher natively only transforms individual blocks. 

In CBC mode, each ciphertext block is added to the next plaintext block before the 
next call to the cipher core. 

The first plaintext block, which has no associated previous ciphertext block, is added
to a "fake 0th ciphertext block" called the initialization vector, or IV. 

Implement CBC mode by hand by taking the ECB function you wrote earlier, making it encrypt
instead of decrypt (verify this by decrypting whatever you encrypt to test), and 
using your XOR function from the previous exercise to combine them. 

The file here is intelligible (somewhat) when CBC decrypted against "YELLOW SUBMARINE"
with an IV of all ASCII 0 (\x00\x00\x00 &c)
'''

from base64 import b64decode
from Crypto.Cipher import AES
from challenge7 import decrypt_AES_128_ECBmode
from challenge5 import encrypt

def encrypt_AES_128_ECBmode(text, key):
	return AES.new(key, AES.MODE_ECB).encrypt(text)

def test_encrypt_AES_128_ECBmode(text, key):
	return decrypt_AES_128_ECBmode(encrypt_AES_128_ECBmode(text, key), key) == text

def xor(data1, data2):
	if (len(data1) != len(data2)):
		raise ValueError('xor arguments must have the same length')

	xor_results = b''
	for a, b in zip(data1, data2):
		xor_results += bytes([chr(ord(a) ^ ord(b))])

	return xor_results


def decrypt_aes_cbc(text, key, IV):
	plaintext = b''
	temp = IV

	for i in range(0, (len(text)/16)):
		block = text[i*16: i*16 + 16]
		decrypted_block = decrypt_AES_128_ECBmode(block, key)
		plaintext_block = xor(decrypted_block, temp)
		plaintext+= plaintext_block
		temp = block

	return plaintext

def main():
	file = 'data/text_challenge10.txt'
	with open(file) as input:
		text = b64decode(input.read())

	# Verify encrypt function 
	assert(test_encrypt_AES_128_ECBmode("Emily Margaret L", "YELLOW SUBMARINE"))

	key = b'YELLOW SUBMARINE'
	IV = b'\x00' * 16

	plaintext = decrypt_aes_cbc(text, key, IV)

	print "Final plaintext: ", plaintext

if __name__ == '__main__':
	main()