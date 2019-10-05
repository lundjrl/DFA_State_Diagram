#!/usr/bin/env python3
#Alphabet = {000, .... 999}
#L={w|w contains an even number of the two letter sequence 105102 and an odd number of the five letter sequence 119104105108101}

#Output should be a sequence of states that the machine goes through; an output of ACCEPT or REJECT depending on the input string.

class DFA:
    print("Please enter a file")
    input = input()
    # Loop through file and delete newline characters
    with open(input, 'r') as file:
        data = file.read().replace('\n', '')

    i = 0
    j = 3
    for char in data:
        print("Start State")
        # Start to process "105102" even num of times
        if data[i:j] == '105':
            print("State Q1")
            i += 3
            j += 3
            if data[i:j] == '102':
                print("State Q2")
                i += 3
                j += 3

        # Start to process "119104105108101" odd number of times
        if data[i:j] == '119':
            print("State Q3")
            i += 3
            j += 3
            if data[i:j] == '104':
                print("State Q4")
                i += 3
                j += 3
                if data[i:j] == '105':
                    print("State Q5")
                    i += 3
                    j += 3
                    if data[i:j] == '108':
                        print("State Q6")
                        i += 3
                        j += 3
                        if data[i:j] == '101':
                            print("ACCEPT")
                            exit(0)

    print("REJECT")

