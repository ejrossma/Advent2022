#Day 2 of Advent of Code 2022

#input is rock paper scissors moves ABC is in first column and what the opponent will "choose"
#XYZ is the second column and what the player should choose

def rock_paper_scissors(input_file):
    dict = {
        'A' : 1, #Rock 1
        'B' : 2, #Paper 2
        'C' : 3, #Scissors 3

        'X' : 1, #Rock 1
        'Y' : 2, #Paper 2
        'Z' : 3  #Scissors 3
    }

    file = open(input_file)
    score = 0
    for x in file:
        input = x.split()
        opp = dict[input[0]]
        player = dict[input[1]]

        if player == opp: #draw
            score = score + player + 3
        elif (player == 1 and opp == 3) or (player == 2 and opp == 1) or (player == 3 and opp == 2): #player wins
            score = score + player + 6
        else: #loss
            score += player
    return score

def rock_paper_scissors_part_two(input_file):
    dict = {
        'A' : 1, #Rock 1
        'B' : 2, #Paper 2
        'C' : 3, #Scissors 3

        'X' : 1, #Rock 1
        'Y' : 2, #Paper 2
        'Z' : 3  #Scissors 3
    }

    file = open(input_file)
    score = 0
    for x in file:
        input = x.split()
        opp = dict[input[0]]
        outcome = dict[input[1]]

        if outcome == 1: #lose
            if opp == 1: #scissors losing to rock
                score += 3 
            elif opp == 2: #rock losing to paper
                score += 1 
            else: #paper losing to scissors
                score += 2 
        elif outcome == 2: #draw
            score = score + opp + 3
        elif outcome == 3: #win
            if opp == 1: #paper beating rock
                score += 2 + 6 
            elif opp == 2: #scissors beating paper
                score += 3 + 6
            else: #rock beating scissors
                score += 1 + 6
    return score
    

if __name__ == "__main__":
    print(rock_paper_scissors("input.txt"))
    print(rock_paper_scissors_part_two("input.txt"))
