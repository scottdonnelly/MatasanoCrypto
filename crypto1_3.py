

import pprint


a = "7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f"
a = [a[i:i+2] for i in range(0, len(a), 2)]



def byteDecode(a, num):
	xor= int(a, 16) ^ int(num, 16)
	hexchar = "%x" % xor

	try: 
		char = hexchar.decode("hex")
	except TypeError:
	 	char = ''
	return char


def XORfunc(num):
	word = [byteDecode(i, num) for i in a]
	word = "".join(word)
	return word


bytes = [hex(i) for i in range(128)]

results = [XORfunc(i) for i in bytes]

