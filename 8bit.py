# input - a string of characters of any length
# output - nestedlist containing 64bit size  

#convert a string to its binary form and store it in a list
a = 'abcdef'
a = [[int(i) for i in bin(x)[2:]] for x in a.encode('utf-8')]
print(a)

#zero-padding
for i in a:
	while len(i) < 8:
		i.insert(0,0)

#null padding
a = [ i for sublist in a for i in sublist]
while(len(a) < 64):
	a.append(0)

print(a)
