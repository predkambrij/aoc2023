
def game_val(game_line):
    game_num_inf, game_inf = game_line.split(":")
    game_num = int(game_num_inf.split(" ")[1])

    color_red_max=0
    color_green_max=0
    color_blue_max=0

    for set_val in game_inf.split(";"):
        for numcolor_val in set_val.strip().split(","):
            num_val, color_val = numcolor_val.strip().split(" ")
            if "red" == color_val:
                if int(num_val) > color_red_max:
                    color_red_max = int(num_val)
            if "green" == color_val:
                if int(num_val) > color_green_max:
                    color_green_max = int(num_val)
            if "blue" == color_val:
                if int(num_val) > color_blue_max:
                    color_blue_max = int(num_val)

    return color_red_max*color_green_max*color_blue_max


sum=0
#f = open("samplerecord.txt", "rt")
f = open("part1.txt", "rt")
for game_line in f:
    val = game_val(game_line)
    sum += val

print(sum)


# 10 min
