

import itertools as iter


a = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"


def breakToBytes(string):
    raw_bytes = [string[i:i+2] for i in range(0, len(string), 2)]
    return raw_bytes
    

def byteEncode(str_byte, key_letter):
	xor= int(str_byte, 16) ^ int(key_letter.encode("hex"), 16)
	hexchar = "%x" % xor
	return hexchar


def repeatingXOR(unencrypted_string, key):
    encrypted_result = []
    key_letter = iter.cycle(key)
    for i in unencrypted_string:
        encrypted_byte = byteEncode(i, next(key_letter))
        encrypted_result.append(encrypted_byte)
    return "".join(encrypted_result)
        

def main(string, key = "ICE"):
    string = breakToBytes(string.encode("hex"))
    result = repeatingXOR(string, key)
    print result
    
main(a)










