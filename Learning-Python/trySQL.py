import sqlite3
import sys

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

#  sample file name => mbox-short.txt
fname = sys.argv[1] if len(sys.argv) >= 2 else input('Enter file name: ')
fh = open(fname)

for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    org = email[email.index('@')+1:]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    # cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(org,))
conn.commit()

result = cur.execute('SELECT * FROM Counts ORDER BY count DESC') 
for row in result:
    print(str(row[0]), row[1])

# print('\n----------------------------')
# final = cur.execute('select org, count(*) from Counts group by org order by count(*) desc')  
# for row in final:
#     print(str(row[0]), row[1])  
# print('\n----------------------------')

cur.close()