'''
Challenge 9: Implement PKCS#7 padding

A block cipher transforms a fixed-size block (usually 8 or 16 bytes) of plaintext
into ciphertext. But we almost never want to transform a single block; we encrypt 
irregularly-sized messages. 

One way we account for irregularly-sized messages is by padding, creating a plaintext
that is an even multiple of the blocksize. The most popular padding scheme is called PKCS#7. 

So: pad any block to a specific block length, by appending the number of bytes of padding to
the end of the block. 

For instance, "YELLOW SUBMARINE" ...padded to 20 bytes would be: 
"YELLOW SUBMARINE\x04\x04\x04\x04"
'''

def pkcsPadding(s, blockSize):
	leftovers = len(s) % blockSize
	s += "\x04"*(blockSize - leftovers)
	return s

def main():
	padded = pkcsPadding("YELLOW SUBMARINE", 20)
	print "Padded string: "
	print padded

if __name__ == '__main__':
	main()