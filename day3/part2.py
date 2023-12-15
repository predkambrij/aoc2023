
from math import exp

#sum=0
name="sample_input.txt"
name2="input1.txt"
f = open(name2, "rt")
f2 = open(name2, "rt")

numbers_with_indexes=[]
row=0
for engine_line in f:
    current_number_stream=""
    current_number_stream_index1=0
    current_number_stream_index2=0
    for engine_character, index in zip((x for x in engine_line), range(len(engine_line))):
        if (engine_character.isdigit()):
            if current_number_stream == "":
                current_number_stream_index1=index
            current_number_stream = current_number_stream+engine_character
            current_number_stream_index2=index
        else:
            if current_number_stream != "":
                numbers_with_indexes.append(tuple([current_number_stream, current_number_stream_index1, current_number_stream_index2, row]))
                current_number_stream=""
                current_number_stream_index1=0
                current_number_stream_index2=0
    row+=1
print(numbers_with_indexes)

def isSymbol(matrix_val):
    return matrix_val == "*"

def checkNumberForPart(number, start_i, end_i, row_i):
    if start_i == 0:
        start_check = 0
    else:
        start_check = start_i - 1
        # check middle row
        if isSymbol(input_matrix[row_i][start_check]):
            addOrIncrementGear(row_i, start_check, number)
            return 1
    if end_i == (matrix_width-1):
        stop_check = end_i
    else:
        stop_check = end_i + 1
        # check middle row
        if isSymbol(input_matrix[row_i][stop_check]):
            addOrIncrementGear(row_i, stop_check, number)
            return 1

    if row_i != 0:
        # check previous line
        for check_i in range(start_check, stop_check+1):
            if isSymbol(input_matrix[row_i-1][check_i]):
                addOrIncrementGear(row_i-1, check_i, number)
                return 1
    if row_i != (len(input_matrix)-1):
        # check next line
        for check_i in range(start_check, stop_check+1):
            if isSymbol(input_matrix[row_i+1][check_i]):
                addOrIncrementGear(row_i+1, check_i, number)
                return 1
    return 0

def addOrIncrementGear(row, index, num):
    global gears
    found_gear=None
    for gear in gears:
        if gear[0] == row and gear[1] == index:
            found_gear=gear
            break

    if not found_gear:
        found_gear=[row, index, [num]]
        gears.append(found_gear)
    else:
        found_gear[2].append(num)


gears=[]

engine_parts=[]
input_matrix = f2.read().split("\n")
matrix_width=len(input_matrix[0])
for number, start_i, end_i, row_i in numbers_with_indexes:
    res = checkNumberForPart(number, start_i, end_i, row_i)
    if (res > 0):
        engine_parts.append(number)
        #sum += int(number)
        #print("num "+str(number))
    else:
        #print("excluded "+str(number))
        pass

sum2=0
for gear in gears:
    if (len(gear[2])==2):
        print(gear)
        mulres = int(gear[2][0]) * int(gear[2][1])
        sum2 += mulres

print(sum2)

# 32 min
