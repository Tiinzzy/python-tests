import urllib.request, urllib.parse, urllib.error

fileHandle = urllib.request.urlopen('htt://data.pr4e.org/romeo.txt')

counts = dict()
for line in fileHandle:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0)+1
print(counts)