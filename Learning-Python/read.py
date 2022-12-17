# Use words.txt as the file name
fname = input("Enter file name: ")
try :
    fh = open(fname)
except :
    print("invalid filte, try again", fh)
    quit()
for text in fh :
    text = text.rstrip().upper()
    print(text)
