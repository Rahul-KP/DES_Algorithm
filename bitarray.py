class bitarray:
      def __init__(self, hex_in):
            self.bits = [int(x) for x in bin(int(hex_in, 16))[2:]]

      def zero_padding(self):
            while(len(self) < 64):
                  i = 0
                  self.bits.insert(i,0)

      def permute(self, perm_list):
            self.bits = [self[perm_list[i]-1] for i in range(len(perm_list))]

      def split_half(self):
            self.bits = [self[i:i+len(self)//2] for i in range(0,len(self),len(self)//2)]

      def group_by(self, no_of_bits):
            self.bits = [self[i:i+6] for i in range(0, len(self), 6)]

      def lcs(self):
            self.bits.append(self[0])
            self.bits.remove(self[0])

      def XOR(self, obj):
            self.bits = [self[i] ^ obj[i] for i in range(len(obj))]

      def __getitem__(self, index):
            return self.bits[index]

      def __setitem__(self, index, value):
            self.bits[index] = value

      def __add__(self, other):
            return self.bits + other.bits

      def __len__(self):
            return len(self.bits)

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
