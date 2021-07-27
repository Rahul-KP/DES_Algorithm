from bitarray import *

#S-boxes
def bin_to_dec(inp):
    c = len(inp) - 1
    d = 0
    for i in inp:
        d += 2**c * i
        c -= 1
    return d

def dec_to_bin(inp):
    binlist = []
    while inp > 0:
        binlist.append(inp % 2)
        inp /= 2
    binlist.reverse()
    return binlist
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

# K = bitarray('rahul').get_bytes()
string_64 = '0001001100110100010101110111100110011011101111001101111111110001' #key as 64 binary bits
K = list(string_64)
K = [int(i) for i in K] #converting the string of 64-bit key to a list of 64 bits of datatype 'int'

#Zero padding
while(len(K) < 64):
	i = 0
	K.insert(i,0)
	i += 1

#PC-1
pc1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]

#Applying PC-1
# key_plus = [] #aka permuted key ,k+
key_plus = permutation(K,pc1)

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

# XOR_lists() - to find XOR of 2 different lists of same size
#e_r - E(Rn-1) ie expanded Rn-1
#k - nth key ,kn
#XORed - list of bits from E(Rn-1) XORed with kn 
def XOR_lists(e_r,k):
	XORed = [e_r[i] ^ k[i] for i in range(len(k))]
	return XORed

def s_boxes(s_inp):
    S1 = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
    S2 = [[15,1,8,4,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
    S3 = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]
    S4 = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]
    S5 = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]
    S6 = [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]
    S7 = [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]
    S8 = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]

    S = [S1] + [S2] + [S3] + [S4] + [S5] + [S6] + [S7] + [S8]
    B = [s_inp[i:i+6] for i in range(0, len(s_inp), 6)]
    s_out = []
    for k in B:
        i = bin_to_dec([k[0], k[-1]])
        j = bin_to_dec(k[1:-1])
        s_out.extend(dec_to_bin(S[B.index(k)][i][j]))
    return s_out

#cipher_16 - A function to iterate through the split IP and hence find f(cipher before inverse permutation)
def cipher_16(IP):
    L = IP[0]
    R = IP[1]
    P = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]
    for i in range(16):
        Ln = R #Rn-1 = R
        s_input = XOR_lists((permutation(R,E_bit_table)),keys[i]) #48 bit input to S boxes
        s_output = s_boxes(s_input) # 32 bit output from S boxes, have to undergo permutation P
        s_output = permutation(s_output, P)
        Rn = XOR_lists(L, s_output)
        R = Rn
        L = Ln
    return [L,R]

L16, R16 = cipher_16(IP_bits)

pass
pass
