
sum=0
#f = open("part2sample.txt", "rt")
f = open("input2.txt", "rt")

txtnumbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
txtnumbersdic = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

for line in f:
    digits = []
    for x in zip((u for u in line), range(len(line))):
        if x[0].isdigit():
            digits.append(int(x[0]))
            continue
        for txtnum in txtnumbers:
            if line[x[1]:].startswith(txtnum):
                digits.append(txtnumbersdic[txtnum])
                break

    #print(digits)
    #   digits = [c for c in line  if c.isdigit()]
    numstr = "".join(str(x) for x in [digits[0],digits[-1]])
    num = int(numstr)
    sum += num
print(sum)

