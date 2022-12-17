fname = input("Enter file name: ")
fh = open(fname)

lst = list()
names = dict()
for line in fh :
    if not line.startswith('From ') : continue
    line = line.strip()
    word = line.split('From ')
    email = word[1]
    pieces = email.split()[0]
    lst.append(pieces)
for p in lst :
    names[p] = names.get(p,0)+1
       
bigCount = None
bigName = None
for word,count in names.items() :
     if bigCount is None or count > bigCount :
            bigName = word
            bigCount = count
print(bigName, bigCount)        