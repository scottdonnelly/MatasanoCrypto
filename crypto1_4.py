
import pprint as pr
from nltk.corpus import stopwords


byte_keys = [hex(i) for i in range(128)]

with open("4.txt") as f:
    start_list = [line.strip() for line in f]

#break hex string to bytes
def breakToBytes(string):
    raw_bytes = [string[i:i+2] for i in range(0, len(string), 2)]
    return raw_bytes
    
#run XOR on individual bytes
def byteDecode(a, num):
	xor= int(a, 16) ^ int(num, 16)
	hexchar = "%x" % xor
	try: 
		char = hexchar.decode("hex")
	except TypeError:
	 	char = ''
	return char

#takes individual hex for checking. returns decoded post-XOR results
def XORfunc(encrypted_str, num):
	word = [byteDecode(i, num) for i in encrypted_str]
	word = "".join(word)
	return word

#checks for English stop words
def checkEnglish(res):
    s=set(stopwords.words('english'))
    possibles = []
    for word in s:
        for string in res:
            #print word, string
            if len(word) > 2 and word.encode() in string:
                possibles.append(string)
    if len(possibles) > 0:
        return possibles
    else:
        pass

def decrypt():
    encrypted_list = [breakToBytes(i) for i in start_list]
    decrypted_list = []
    for j in encrypted_list:
        decrypted_strings = [XORfunc(j,byte) for byte in byte_keys]
        decrypted_list.append(decrypted_strings)
    return decrypted_list


def main():
    decrypted_list = decrypt()
    #pr.pprint([i for i,s in enumerate(decrypted_list) for j in s if "Now " in j])
    possible_words = [checkEnglish(i) for i in decrypted_list]
    possible_words = filter(lambda x: x is not None, possible_words)
    print possible_words

main()



