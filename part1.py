#!/usr/bin/env python3
#Alphabet = {000, .... 999}
#L={w|w contains an even number of the two letter sequence 105102 and an odd number of the five letter sequence 119104105108101}

#Output should be a sequence of states that the machine goes through; an output of ACCEPT or REJECT depending on the input string.


# The if statements in this program are the transitions when fulfilled
# and prints indicate the current state you are in. 
# The end of the loop prints whether the word you are processing is a 
# part of the language or not. 
class DFA:
    print("Please enter a file")
    countone = 0
    counttwo = 0
    input = input()
    # Loop through file and delete newline characters
    with open(input, 'r') as file:
        data = file.read().replace('\n', '')

    i = 0
    j = 3
    print("Start State")
    length = int(len(data) / 3)
    print(length)
    for char in range(0, length, 3):
        # Start to process "105102" even num of times
        if data[i:j] == '105':
            print("State Q1")
            i += 3
            j += 3
            if data[i:j] == '102':
                print("State Q2")
                i += 3
                j += 3
                countone += 1
                if data[i:j] == '105':
                    print("State Q3")
                    i += 3
                    j += 3
                    if data[i:j] == '102':
                        print("Start State")
                        i += 3
                        j += 3
                        countone += 1

        # Start to process "119104105108101" odd number of times
        elif data[i:j] == '119':
            print("State Q4")
            i += 3
            j += 3
            if data[i:j] == '104':
                print("State Q5")
                i += 3
                j += 3
                if data[i:j] == '105':
                    print("State Q6")
                    i += 3
                    j += 3
                    if data[i:j] == '108':
                        print("State Q7")
                        i += 3
                        j += 3
                        if data[i:j] == '101':
                            counttwo += 1 
                            print("State Q8")
                            i += 3
                            j += 3
                            #if (counttwo % 2) != 0 and (countone % 2) == 0:
                            #    print("ACCEPT")
                            #    exit(0)
                            #else:
                            #    print("REJECT")
                            #    exit(0)

        else:
            print("Start State")
            i += 3
            j += 4

    if (countone % 2) == 0 and (counttwo % 2) != 0:
        print("ACCEPT")
    elif (countone % 2) == 0 or (counttwo % 2) == 0:
        print("REJECT")
    elif (counttwo % 2) == 0 and (countone % 2) != 0:
        print("REJECT")
