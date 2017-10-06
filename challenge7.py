'''
Challenge 7: AES in ECB mode

The Base64-encoded content in this file has been encrypted via AES-128 in ECB 
mode under the key. 

"YELLOW SUBMARINE".

(case-sensitive, without the quotes; exactly 16 characters; I like "YELLOW
	SUBMARINE" because it's exactly 16 bytes long, and now you do too).

Decrypt it. You know the key, after all. 

Easiest way: use OpenSSL::Cipher and give it AES-128-ECB as the cipher.
'''

from binascii import a2b_base64
from Crypto.Cipher import AES

KEY = "YELLOW SUBMARINE"

def decrypt_AES_128_ECBmode(text, key):
	return AES.new(key, AES.MODE_ECB).decrypt(text)

def main():
	file = 'data/text_challenge7.txt'
	text = ""
	for line in open(file):
		text += line.strip()
	text = a2b_base64(text)

	# TODO: implement without built-in func
	decoded_data = decrypt_AES_128_ECBmode(text, KEY)
	print decoded_data

if __name__ == '__main__':
	main()