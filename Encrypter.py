from bitarray import *

#function to perform permutations
def permutation(inp_list, perm_list): #prem_list - permuted list
    new_list = [inp_list[perm_list[i]-1] for i in range(len(perm_list))]
    return new_list

# function to split a given list into two halves
def split_half(tmp_list):
	tmp_list = [tmp_list[i:i+len(tmp_list)//2] for i in range(0,len(tmp_list),len(tmp_list)//2)]
	return tmp_list

# Left Circular shift function
def lcs(tmp_list):
	tmp_list.append(tmp_list[0])
	tmp_list.remove(tmp_list[0])
	return tmp_list

def round_of_16(key_plus):

	keys = [] #16 keys of 56bits each

	c = key_plus[0]# 28 bits
	d = key_plus[1]
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
string_data64 = '0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111'
string_data64 = string_data64.split()
string_data64 = list(''.join(string_data64))
M = [int(i) for i in string_data64]

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
# key_plus = [] #aka permuted key ,k+
key_plus = permutation(key_64,pc1)

key_plus = split_half(key_plus)

#16 subkeys are obtained ,each of 56 bits
keys = round_of_16(key_plus) 

#PC2
pc2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
#calling function to perform PC2 permutation
#Here each key becomes 48 bits in length
for i in range(len(keys)):
    keys[i] = permutation(keys[i], pc2)

#Initial Permutation
ip_table = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

#IP - bits 
IP_bits = split_half(permutation(M, ip_table)) #L0 and R0 are obtained from split_half()

#E-bit Selection table , where E stands for Expansion  
E_bit_table = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]

#cipher_16 - A function to iterate through the split IP and hence find f(cipher before inverse permutation)
def cipher_16(IP):
	L = IP[0]
	R = IP[1]
	for i in range(16):
		Ln = R
		Rn = L ^ f((permutation(R,E_bit_table)),keys[i])

# f() - to find f(cipher before inverse permutation)
#e_r - E(Rn-1) ie expanded Rn-1
#k - nth key ,kn
#XORed - list of bits from E(Rn-1) XORed with kn 
def f(e_r,k):
	XORed = [e_r ^ k for i in range(len(k))]
	


