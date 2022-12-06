#Day 5 of Advent of Code 2022

#take in the base configuration
    #gotta make a list of crates for each number

#go number by number
    #Each letter after the first one is separated by 3 characters
        #while not end of line skip 3 and check for letter

#getting number of crates      

def supply_stacks(input_file):
    file = open(input_file)
    line = file.readline()
    
    crates = []
    ind = 1
    num_crates = 0
    
    while ind < len(line): #initial loop to get size and setup crates
        crate = []
        if line[ind].isalpha():
            crate.append(line[ind])
        crates.append(crate)
        ind += 4
        num_crates += 1

    #then loop through all of the base setup
    while line != "\n":
        line = file.readline()
        ind = 1
        crate_num = 0
        while ind < len(line):
            if line[ind].isalpha():
                crates[crate_num].append(line[ind])
            ind += 4
            crate_num += 1

    #loop through all of the instructions
    for line in file:
        instruct = line.strip().split()
        num_to_move = int(instruct[1])
        #need to turn to ints and adjust for array indexing
        start_pos = int(instruct[3]) - 1
        finish_pos = int(instruct[5]) - 1
        #move crate
        for i in range(num_to_move):
            temp_letter = crates[start_pos][0]
            crates[start_pos].pop(0)
            crates[finish_pos].insert(0, temp_letter)

    output = ""
    for c in crates:
        output += c[0]
    return output

def supply_stacks_part_two(input_file):
    file = open(input_file)
    line = file.readline()
    
    crates = []
    ind = 1
    num_crates = 0
    
    while ind < len(line): #initial loop to get size and setup crates
        crate = []
        if line[ind].isalpha():
            crate.append(line[ind])
        crates.append(crate)
        ind += 4
        num_crates += 1

    #then loop through all of the base setup
    while line != "\n":
        line = file.readline()
        ind = 1
        crate_num = 0
        while ind < len(line):
            if line[ind].isalpha():
                crates[crate_num].append(line[ind])
            ind += 4
            crate_num += 1

    #loop through all of the instructions
    for line in file:
        instruct = line.strip().split()
        num_to_move = int(instruct[1])
        #need to turn to ints and adjust for array indexing
        start_pos = int(instruct[3]) - 1
        finish_pos = int(instruct[5]) - 1
        #move crate
        crate_queue = []
        for i in range(num_to_move):
            temp_letter = crates[start_pos][0]
            crate_queue.insert(0, temp_letter)
            crates[start_pos].pop(0)
        
        for c in crate_queue:
            crates[finish_pos].insert(0, c)
            

    output = ""
    for c in crates:
        output += c[0]
    return output



if __name__ == "__main__":
    print(supply_stacks("input.txt"))
    print(supply_stacks_part_two("input.txt"))