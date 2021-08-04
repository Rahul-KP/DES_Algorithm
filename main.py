from bitarray import *

#round_of_16() - to create 16 keys
def round_of_16(key_plus):

	keys = [] #16 keys of 56bits each

	c = key_plus[0]# 28 bits
	d = key_plus[1]
	one_lcs = [1,2,9,16]
	for i in range(1,17):
		if i in one_lcs:
			c.lcs()
			d.lcs()
			keys.append(c+d)
		else:
			for i in range(2):
				c.lcs()
				d.lcs()
			keys.append(c+d)
	return keys

#cipher_16 - A function to iterate through the split IP and hence find f(cipher before inverse permutation)
def cipher_16(IP, E_bit_table, keys_16):
    L = IP[0]
    R = IP[1]
    P = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]
    #print(hex(bin_to_dec(L))[2:],hex(bin_to_dec(R))[2:])
    for i in range(16):
        Ln = R.copy() #Rn-1 = R
        R.permute(E_bit_table)
        R.XOR(keys_16[i]) #48 bit input to S boxes ,aka Kn + E(Rn-1)
        s_output = s_boxes(R) # 32 bit output from S boxes, have to undergo permutation P
        s_output.permute(P)
        L.XOR(s_output) #L contains the result of the final operation in the respective iteration
        #print(hex(bin_to_dec(Ln))[2:],hex(bin_to_dec(Rn))[2:],hex(bin_to_dec(keys[i]))[2:])
        R = L
        L = Ln
    return R,L

#S-boxes
def s_boxes(s_inp):
    S1 =  [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7], [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8], [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
    S2 =  [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10], [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5], [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15], [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
    S3 =  [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8], [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1], [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7], [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
    S4 =  [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15], [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9], [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4], [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]
    S5 =  [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9], [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6], [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14], [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]
    S6 =  [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11], [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8], [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6], [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]
    S7 =  [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1], [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6], [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2], [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]
    S8 =  [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7], [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2], [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8], [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
    S = [S1] + [S2] + [S3] + [S4] + [S5] + [S6] + [S7] + [S8]
    B = bitarray.group_by(s_inp,6)#011000 010001 011110 111010 100001 100110 010100 100111
    s_out = bitarray()# 32 bits
    for k in range(len(B)):
        i = s_out.bin_to_dec([B[k][0], B[k][-1]])
        j = s_out.bin_to_dec(B[k][1:-1])
        s_out.extend(bitarray.dec_to_bin(S[k][i][j], 4))
    return s_out

#Resources
#PC1
pc1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]

#PC2
pc2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

#Initial Permutation
ip_table = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

#E-bit Selection table , where E stands for Expansion
E_bit_table = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

#IP inverse table
IP_inv = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]


def crypt(flag):
    global pc1, pc2, ip_table, E_bit_table, IP_inv
    plain_text = bitarray(input('Enter plaintext in hex: '))
    key = bitarray(input('Enter key in hex : '))

    plain_text.zero_padding()
    key.zero_padding()

    plain_text_org = plain_text.copy()
    key_org = key.copy()

    key.permute(pc1)
    key = bitarray.split_half(key)
    keys_16 = round_of_16(key)

    if flag:
        keys_16.reverse()

    for i in keys_16:
        i.permute(pc2)

    plain_text.permute(ip_table)
    IP_bits = bitarray.split_half(plain_text)

    R16,L16 = cipher_16(IP_bits, E_bit_table, keys_16)
    reverse = R16 + L16

    reverse.permute(IP_inv)

    cipher_text = hex(bitarray.bin_to_dec(reverse.bits))
    plain_text = hex(bitarray.bin_to_dec(plain_text_org.bits))
    key_text = hex(bitarray.bin_to_dec(key_org.bits))
    print('Plain text(hex): ' + plain_text[2:] + '\nKey(hex): ' + key_text[2:] + '\nCipher text(hex): ' + cipher_text[2:])

if __name__ == '__main__':
    flag = input('1. Encrypt\n2. Decrypt\n> ')
    crypt(flag)
