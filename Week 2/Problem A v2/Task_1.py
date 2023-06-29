import sys
sys.setrecursionlimit(10000)

n = 3
x = [None] * n

def combination(i):
    options = [0, 1]
    if i == n: # start with base case
        print(x) # print out whenever an array x is complete
    else:
        for option in options: # start with the first option
            x[i] = option 
            combination(i+1) # recursively move on to the next index

combination(0) #start at index 0