fname = input("Enter file name: ")
fh = open(fname)
lst = list()
final = list()
for line in fh:
    line = line.rstrip()
    result = line.split()
    for i in result:
        if i not in lst :
            lst.append(i)
            lst.sort()
    
        
print(lst)