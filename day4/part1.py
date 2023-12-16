name="sample.txt"
name2="input1.txt"
f = open(name2, "rt")

total_score = 0
for card in f:
    card_numbers = card.strip().split(":")
    winning_numbers__card_numbers = card_numbers[1].split(" | ")

    winning_numbers = [ int(x) for x in winning_numbers__card_numbers[0].strip().split(" ") if x != "" ]
    card_numbers = set([ int(x) for x in winning_numbers__card_numbers[1].strip().split(" ") if x != "" ])

    count = 0
    for winning_number in winning_numbers:
        if winning_number in card_numbers:
            count += 1

    score = 0
    if (count > 0):
        score = 2**(count-1)

    #print(count)
    print(score)
    total_score += score
print()
print(total_score)

    #print(winning_numbers)
    #print(card_numbers)





