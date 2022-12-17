name = input("Enter file:")

handle = open(name)

lst = list()
times = dict()
for line in handle :
    if not line.startswith('From ') : continue
    line = line.strip('From')
    word = line.split()
    time = word[4]
    timespl=time.split(':')[0]
    lst.append(timespl)
for p in lst :
    times[p] = times.get(p,0)+1

for k,v in sorted(times.items()) :
    print(k,v)