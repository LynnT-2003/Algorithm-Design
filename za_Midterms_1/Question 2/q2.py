def can_complete_circuit(Petrol, Distance):
    remaining, starting_station = 0, 0

    for i in range(len(Petrol)):
        remaining += Petrol[i] - Distance[i]

        if remaining < 0:
            remaining = 0
            starting_station = i + 1

    return starting_station    

# Input
N = int(input())
Petrol = list(map(int, input().split()))
Distance = list(map(int, input().split()))

# Output
starting_station = can_complete_circuit(Petrol, Distance)
print(starting_station)