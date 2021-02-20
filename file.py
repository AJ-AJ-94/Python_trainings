xfile = open("C:/Users/Aleksandra/Documents/Swiadkowa.txt")

for line in xfile:
    line = line.rstrip()
    if not '2' in line:
        continue
    print(line)

inl = xfile.read()
print(len(inl))

fchar = inl.find('1')
lchar = inl.find('2')

print(fchar, lchar)

print(inl[0:25])

