from bitarray import *

# function to split a given list into two halves
def split_half(tmp_list):
	tmp_list = [tmp_list[i:i+len(tmp_list)//2] for i in range(0,len(tmp_list),len(tmp_list)//2)]
	return tmp_list

# Left Circular shift function
def lcs(tmp_list):
	tmp_list.append(tmp_list[0])
	tmp_list.remove(tmp_list[0])
	return tmp_list

def round_of_16(key_56):

	keys = [] #16 keys of 56bits each

	c = key_56[0]# 28 bits
	d = key_56[1]
	one_lcs = [1,2,9,16]
	for i in range(1,17):
		if i in one_lcs:
			c = lcs(c)
			d = lcs(d)
			keys.append(c+d)
		else:
			for i in range(2):
				c = lcs(c)
				d = lcs(d)
			keys.append(c+d)
	return keys

#Input data
# key_64 = bitarray('rahul').get_bytes()
string_64 = '0001001100110100010101110111100110011011101111001101111111110001' #key as 64 binary bits
key_64 = list(string_64)
key_64 = [int(i) for i in key_64] #converting the string of 64-bit key to a list of 64 bits of datatype 'int'

#Zero padding
while(len(key_64) < 64):
	i = 0
	key_64.insert(i,0)
	i += 1

#PC-1
pc1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]

#Applying PC-1
# key_56 = [] #aka permuted key ,k+
key_56 = [key_64[pc1[i]-1] for i in range(56)]

key_56 = split_half(key_56)
#print(key_56)
#key_56 is same as k0 =c0+d0

keys = round_of_16(key_56) #16 subkeys are obtained
print(keys)