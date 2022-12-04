#Day 4 of Advent of Code 2022

#input is range of cleaning IDs for pairs of elves
#need to find how many pairs where one elf has their ID range consumed completely by their partners

def camp_cleanup(input_file):
    file = open(input_file)
    count = 0
    for x in file:
        line = x.strip()
        #extract nums from input
        index = 0
        temp = ""
        nums = []
        while index < len(line):
            if line[index].isdigit(): #if number
                temp += line[index]
            else:
                nums.append(int(temp))
                temp = ""
            index += 1
        nums.append(int(temp))

        #check if those nums fit the criteria
        if (nums[0] <= nums[2] and nums[1] >= nums[3]) or (nums[2] <= nums[0] and nums[3] >= nums[1]):
            count += 1

    return count

def camp_cleanup_part_two(input_file):
    file = open(input_file)
    count = 0
    for x in file:
        line = x.strip()
        #extract nums from input
        index = 0
        temp = ""
        nums = []
        while index < len(line):
            if line[index].isdigit(): #if number
                temp += line[index]
            else:
                nums.append(int(temp))
                temp = ""
            index += 1
        nums.append(int(temp))

        #check if those nums fit the criteria
        #n1 to n2 & n3 to n4
        #4 to 4 & 4 to 6
            #if n1 (4) >= n3 (4) && n1 (4) <= n4 (6) TRUE
        #2nd example
        #2 to 5 & 5 to 7
            #if n1 (2) >= n3 (5) && n1 (2) <= n4 (7) FALSE
            #or
            #if n3 (5) >= n1 (2) && n3 (5) <= n2 (5) TRUE
        if (nums[0] >= nums[2] and nums[0] <= nums[3]) or (nums[2] >= nums[0] and nums[2] <= nums[1]):
            count += 1

    return count

if __name__ == "__main__":
    print(camp_cleanup("input.txt"))
    print(camp_cleanup_part_two("input.txt"))