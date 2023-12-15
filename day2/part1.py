
def game_val(game_line):
    game_num_inf, game_inf = game_line.split(":")
    game_num = int(game_num_inf.split(" ")[1])
    for set_val in game_inf.split(";"):
        for numcolor_val in set_val.strip().split(","):
            num_val, color_val = numcolor_val.strip().split(" ")
            if "red" == color_val:
                if int(num_val) > red_max:
                    return 0
            if "green" == color_val:
                if int(num_val) > green_max:
                    return 0
            if "blue" == color_val:
                if int(num_val) > blue_max:
                    return 0
    return game_num



red_max=12
green_max=13
blue_max=14

sum=0
#f = open("samplerecord.txt", "rt")
f = open("part1.txt", "rt")
for game_line in f:
    val = game_val(game_line)
    sum += val

print(sum)

# 40 min
