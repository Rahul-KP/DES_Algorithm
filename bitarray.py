class bitarray:
      def __init__(self, inp):
            tmp = inp[2:]
            tmp = list(tmp)

      def zero_padding(self): #zero padding to the left
            while(len(self) < 8): # to accept 8-bit block for input function
                  i = 0
                  self.bits.insert(i,0)

      def permute(self, perm_list):
            self.bits = [self[perm_list[i]-1] for i in range(len(perm_list))]

      def lcs(self):
            self.bits.append(self[0])
            self.bits.remove(self[0])

      def XOR(self, obj):
            self.bits = [self[i] ^ obj[i] for i in range(len(obj))]

      def extend(self,inp_ls):
            self.bits = self.bits + inp_ls

      def copy(self):
            return bitarray(self.bits.copy())

      def __getitem__(self, index):
            return self.bits[index]

      def __setitem__(self, index, value):
            self.bits[index] = value

      def __add__(self, other):
            return bitarray(self.bits + other.bits)

      def __len__(self):
            return len(self.bits)

      @staticmethod
      def split_half(obj):
           return [bitarray(obj[i:i+len(obj)//2]) for i in range(0,len(obj),len(obj)//2)]

      @staticmethod
      def group_by(bitarry_obj,no_of_bits):
            return [bitarray(bitarry_obj[i:i+no_of_bits]) for i in range(0, len(bitarry_obj), no_of_bits)]

      @staticmethod
      def dec_to_bin(inp, size):
            binstr = bin(inp)
            binlist = list(binstr[2:])
            binlist = [int(x) for x in binlist]
            i = 0
            while len(binlist) < size:
                  binlist.insert(i,0)
                  i += 1
            return binlist

      @staticmethod
      def bin_to_dec(inp):
            return int(''.join([str(x) for x in inp]), 2)

