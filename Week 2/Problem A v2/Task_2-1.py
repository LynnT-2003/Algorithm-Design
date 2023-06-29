import sys
sys.setrecursionlimit(10000)

n = 3
x = [None] * n
count = 0

def combination(i):
    global count
    options = [0, 1]
    if i == n: # start with base case
        print(x) # print out whenever an array x is complete
        return 1
    else:
        for option in options: # start with the first option
            x[i] = option 
            count += combination(i+1)
            print(count) # recursively move on to the next index
        return count

print(combination(0)) #start at index 0