# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
add = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line = line.rstrip()
    #count = count + 1
    num = line[20:27]
    num = float(num)
    add = add + num
    total = add / 27
    #print(total)
print("Average spam confidence:", total)