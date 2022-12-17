import re

openFile = input("Enter file name: ")
of = open(openFile)
lst = list()

for lines in of:
    lines = lines.strip()
    result = re.findall('[0-9]+', lines)
    lst.append(result)

lst2 = [e for e in lst if e]

flat_list = []
for sublist in lst2:
    for item in sublist:
        flat_list.append(item)

sum = 0
for num in flat_list:
    sum += int(num)

print(sum)
