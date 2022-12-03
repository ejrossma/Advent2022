#Day 3 of Advent of Code 2022

#input is rucksacks and their contents
#each compartment has the same number of items (first half is compartment 1 & second half is compartment 2)
#each letter in the rucksack has a value
#a-z 1 to 26
#A-Z 27 to 52
#have to find the duplicate in each half of each rucksack

def rucksack_reorganization(input_file):
    file = open(input_file)
    outcome = 0
    for x in file: #for each line
        input = []
        line = x.strip()
        for c in line: #put each char into input
            input.append(c)
        
        #split into 2 strings
        half = int(len(input) / 2)
        first = ""
        second = ""
        for i in range(half): #0 to half - 1
            first += input[i]
        for i in range(half, half * 2): #half to half * 2 - 1
            second += input[i]

        #find the duplicate char
        for char in first:
            if char in second:
                print(char)
                if char.isupper(): #need to subtract 'a'
                    outcome += ord(char) - ord('A') + 27
                else:
                    outcome += ord(char) - ord('a') + 1
                break #forgot to put this line because I didn't know there could be duplicates
    return outcome

def rucksack_reorganization_part_two(input_file):
    file = open(input_file)
    outcome = 0
    x, y, z = "", "", ""
    count = 0
    for line in file: #for each line
        count += 1
        if count % 3 == 1:
            x = line.strip()
        elif count % 3 == 2:
            y = line.strip()
        else:
            z = line.strip()
            for c in x:
                if c in y and c in z:
                    if c.isupper(): #need to subtract 'a'
                        outcome += ord(c) - ord('A') + 27
                    else:
                        outcome += ord(c) - ord('a') + 1
                    break
    return outcome
                
if __name__ == "__main__":
    print(rucksack_reorganization("input.txt"))
    print(rucksack_reorganization_part_two("input.txt"))
