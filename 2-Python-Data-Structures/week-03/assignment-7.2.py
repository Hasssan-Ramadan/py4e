# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue

    count+=1
    text = line.rstrip()
    pos = text.find('0')
    print(text)
    total += float(text[pos:])


print("Average spam confidence:", total / count)