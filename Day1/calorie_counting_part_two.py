#Day 1 of Advent of Code 2022

#input is a count of calories each elf is carrying
#each elf's inventory is written one item per line & separated by a blank line
#find the elf with the most calories

def calorie_counting_part_two(input_file):
    file = open(input_file)
    max = max2 = max3 = curr = 0
    for x in file:
        if x != '\n': #if x isn't a blank line add to curr
            curr += int(x)
        else: #if x is a newline then check if the curr is bigger than any of the max
            if curr > max: #if curr > max then need to check if each max is greater than its next
                if max > max2:
                    if max2 > max3:
                        max3 = max2
                    max2 = max
                max = curr
            elif curr > max2:
                if max2 > max3:
                    max3 = max2
                max2 = curr
            elif curr > max3:
                max3 = curr
            curr = 0
            
    return(max + max2 + max3)

if __name__ == "__main__":
    print(calorie_counting_part_two("input.txt"))