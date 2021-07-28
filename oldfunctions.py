def bin_to_dec(inp):
    c = len(inp) - 1
    d = 0
    for i in inp:
        d += 2**c * i
        c -= 1
    return d

def dec_to_bin(inp, size):
    binlist = []
    while inp > 0:
        binlist.append(inp % 2)
        inp = inp // 2
    binlist.reverse()
    while len(binlist) < size:
        i = 0
        binlist.insert(i,0)
        i += 1
    return binlist
def hex_to_dec(inp, base):
    c = len(inp) - 1
    d = 0
    hext = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    for i in inp:
        j = i
        if isinstance(i, str):
            j = hext[i]
        d += base**c * j
        c -= 1
    return d

def dec_to_hex(inp, base):
    hexlist = []
    while inp > 0:
        hexlist.append(inp % base)
        inp = inp // base
    hexlist.reverse()
    hext = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    hext = {v: k for k, v in hext.items()}
    for i in hexlist:
        if i in hext.keys():
            hexlist[hexlist.index(i)] = hext[i]
    return hexlist

print(dec_to_hex(36427, 16))
