name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

hours = dict()
handle = open(name)
for line in handle:
    if not line.startswith('From '):
        continue
    hour = line.split()[5].split(':')[0]
    hours[hour] = hours.get(hour, 0) + 1

for k, v in sorted(hours.items()):
    print(k, v)