name="sample.txt"
name2="input1.txt"
f = open(name2, "rt")

total_numbers = 0
card_points_num = []
for card in f:
    card_numbers = card.strip().split(":")
    card = int(card_numbers[0].split(" ")[-1].strip())
    winning_numbers__card_numbers = card_numbers[1].split(" | ")

    winning_numbers = [ int(x) for x in winning_numbers__card_numbers[0].strip().split(" ") if x != "" ]
    card_numbers = set([ int(x) for x in winning_numbers__card_numbers[1].strip().split(" ") if x != "" ])

    count = 0
    for winning_number in winning_numbers:
        if winning_number in card_numbers:
            count += 1

    #print("card %d count %d" % (card, count))
    card_points_num.append([card, count, 1])

#print(card_points_num)

for card, index in zip((x for x in card_points_num), range(len(card_points_num))):
    print(card[0])
    for repeat in range(card[2]):
        for index2 in range(index+1, index+1+card[1]):
            print(index2)
            card_points_num[index2][2] += 1
    print()

print(card_points_num)
print(sum(x[2] for x in card_points_num))





    #print(winning_numbers)
    #print(card_numbers)

# part1+part2 = 50 min



