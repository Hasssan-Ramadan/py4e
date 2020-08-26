import re

file = open('regex_sum_917309.txt')

text = file.read()
numbers = re.findall(r'[0-9]+', text)

total = 0
for num in numbers:
    total += int(num)

print(total)