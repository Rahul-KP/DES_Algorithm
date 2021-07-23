from bitarray import *

#Input data
# data_64 = bitarray('rahul').get_bytes()
string_64 = '0001001100110100010101110111100110011011101111001101111111110001'
data_64 = list(string_64)
data_64 = [int(i) for i in data_64]
# print(data_64)

#Zero padding
while(len(data_64) < 64):
	i = 0
	data_64.insert(i,0)
	i += 1

#PC-1
pc1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]

#Applying PC-1 
# data_56 = [] #aka permuted key ,k+	 
data_56 = [data_64[pc1[i]-1] for i in range(56)] 

# function to split a given list into two halves
def split_half(tmp_list):
	tmp_list = [tmp_list[i:i+len(tmp_list)//2] for i in range(0,len(tmp_list),len(tmp_list)//2)]
	return tmp_list

data_56 = split_half(data_56)
print(data_56)
#data_56 is same as k0 =c0+d0
# Left Circular shift function
def lcs(tmp_list):
	tmp_list.append(tmp_list[0])
	tmp_list.remove(tmp_list[0])
	return tmp_list

def round_of_16(data_56):

	keys = [] #16 keys of 56bits each

	c = data_56[0]# 28 bits
	d = data_56[1]
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
keys = round_of_16(data_56)
print(keys)