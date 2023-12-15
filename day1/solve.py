
sum=0
#f = open("sample.txt", "rt")
f = open("input.txt", "rt")
for line in f:
    digits = [c for c in line  if c.isdigit()]
    numstr = "".join([digits[0],digits[-1]])
    num = int(numstr)
    sum += num
print(sum)

