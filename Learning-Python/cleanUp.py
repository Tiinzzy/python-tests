fname = input("Enter file name: ")
fh = open(fname)

count = 0
for line in fh :
    line = line.strip()
    if not line.startswith('From ') : continue
    count += 1    
    word = line.split('From ')
    email = word[1]
    pieces = email.split()
    print(email.split( )[0])      
print("There were", count, "lines in the file with From as the first word")
