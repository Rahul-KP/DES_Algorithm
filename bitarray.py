class bitarray:
      def __init__(self, string):
            encoded_bytes = bytes(string, 'utf-8') #(b'hello')
            binary_bytes = [bin(x)[2:] for x in encoded_bytes] #['100001', '101010']
            self.bits = [] #[0, 1, 0, 1, 0, 1]
            #binary_bytes[1] = '00101010'
            for i in binary_bytes: # i is '0101010'
                  while len(i) < 8:
                        i = '0' + i #i will be '00101010'
                  self.bits.extend(list(i))

      def get_bytes(self):
            for i in self.bits:
                  print(i, end=' ')
            print()

string1 = 'rahul'
byte1 = bitarray(string1)
byte1.get_bytes()
