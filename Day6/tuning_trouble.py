#Day 6 of Advent of Code 2022

#have to decipher a signal from input
#signal starts when you get 4 unique characters in a row
#return the index + 1 after finding the 4th character

def tuning_trouble(input_file):
    file = open(input_file)
    line = file.readline().strip()
    ind = 0
    
    while ind < len(line):
        signal = ""
        for i in range(ind, ind + 4):
            if line[i] not in signal:
                signal += line[i]
        if len(signal) == 4:
            return ind + 4
        ind += 1

def tuning_trouble_part_two(input_file):
    file = open(input_file)
    line = file.readline().strip()
    ind = 0
    
    while ind < len(line):
        signal = ""
        for i in range(ind, ind + 14):
            if line[i] not in signal:
                signal += line[i]
        if len(signal) == 14:
            return ind + 14
        ind += 1

        


if __name__ == "__main__":
    print(tuning_trouble("input.txt"))
    print(tuning_trouble_part_two("input.txt"))