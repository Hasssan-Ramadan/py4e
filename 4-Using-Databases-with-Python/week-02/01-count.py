import sqlite3

conn = sqlite3.connect('01-count.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

file = open('mbox.txt')
for line in file:
    if not line.startswith('From: '):
        continue
    domain = line.split()[1].split('@')[1]
    cur.execute('SELECT * FROM Counts WHERE org = ?', (domain,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))

conn.commit()

cur.execute('SELECT * FROM Counts ORDER BY count DESC')
row = cur.fetchone()
print(row)

cur.close()
conn.close()