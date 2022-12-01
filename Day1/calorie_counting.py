#Day 1 of Advent of Code 2022

#input is a count of calories each elf is carrying
#each elf's inventory is written one item per line & separated by a blank line
#find the elf with the most calories

def calorie_counting(input_file):
    file = open(input_file)
    max = curr = 0
    for x in file:
        if x != '\n': #if x isn't a blank line add to curr
            curr += int(x)
        else: #if x is a newline then check if curr > max
            if curr > max:
                max = curr
            curr = 0
    print(max)


calorie_counting("input.txt")