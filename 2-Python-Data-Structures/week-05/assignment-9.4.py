name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)
senders = dict()
for line in handle:
    if not line.startswith('From '):
        continue
    sender = line.split()[1]
    senders[sender] = senders.get(sender,0) + 1

max_mails = 0
max_sender = None

for k, v in senders.items():
    if v > max_mails:
        max_mails = v
        max_sender = k

print(max_sender, max_mails)