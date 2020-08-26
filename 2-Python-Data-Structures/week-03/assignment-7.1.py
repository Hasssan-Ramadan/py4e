fname = input("Enter file name: ")
fh = open(fname)

text = fh.read().rstrip()
print(text.upper())
