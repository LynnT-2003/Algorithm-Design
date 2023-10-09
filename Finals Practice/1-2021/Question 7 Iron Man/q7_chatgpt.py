# Ironman is fighting the Chitauri forces (the villain army in The Avengers 2012). N attacking
# aircrafts of the Chitauri form a circle around Ironman. In each aircraft, there are a number of
# Chitauri soldiers. Ironman’s repulsor can destroy three adjacent aircrafts per one shoot,
# which immediately kills all the soldiers in those aircrafts. However, after the shoot, the
# survival Chitauri soldiers also fire back at Ironman causing some damage to him — one unit
# per soldier. Ironman will further follow with new shoot and so on until all aircrafts are
# destroyed. It is required to define the minimum amount of damage, which can be dangerous
# to Tony Stark.
# INPUT: N integers, amount of soliders on each consecutive aircraft (not less than 1 and no
# more than 100 on each). 3 ≤ N ≤ 20.
# OUTPUT: The minimum amount of damage.
# Elaboration:
# 1) Shoot the 2
# nd aircraft destroys 3+4+2, damage = 2+1+4+1 = 8
# 2) Shoot the 5th aircraft destroys 2+1+4, damage += 1 = 9

def minimum_damage(soldiers):
    n = len(soldiers)
    min_damage = float('inf')

    for i in range(n):
        damage = 0
        for j in range(n):
            if j < i or j >= i + 3:
                damage += soldiers[j]
        
        min_damage = min(min_damage, damage)
    
    return min_damage

# Input: List of integers representing soldiers on each aircraft
input_str = input("Enter the number of soldiers on each consecutive aircraft: ")
soldiers = list(map(int, input_str.split()))

# Calculate and print the minimum amount of damage
result = minimum_damage(soldiers)
print("Minimum amount of damage:", result)

# Explanation:

# def minimum_damage(soldiers):

# This defines a function named minimum_damage that takes a list of integers called soldiers as its parameter. The soldiers list represents the number of soldiers on each consecutive aircraft.
# n = len(soldiers)

# This calculates the length of the soldiers list, which gives us the number of aircraft in the circle. It assigns this value to the variable n.
# min_damage = float('inf')

# min_damage is initialized to positive infinity (float('inf')) to ensure that any calculated damage will be less than this initial value.
# for i in range(n):

# This initiates a loop that iterates through each aircraft in the circle. The variable i represents the current aircraft being considered.
# damage = 0

# Inside the loop, a variable damage is initialized to zero. This variable will be used to calculate the damage for the current shooting strategy.
# for j in range(n):

# This nested loop iterates through all the aircraft in the circle again, using the variable j to represent the current aircraft.
# if j < i or j >= i + 3:

# This conditional statement checks if the current aircraft j is not within the range of three aircraft to the right of the current aircraft i. In other words, it checks if aircraft j is not one of the three aircraft that will be destroyed by the shoot from aircraft i.
# damage += soldiers[j]

# If the condition in the previous step is met, it means the soldiers on aircraft j will fire back at Ironman. The number of soldiers on aircraft j is added to the damage variable to calculate the damage caused by those soldiers.
# min_damage = min(min_damage, damage)

# After calculating the damage for the current shooting strategy, it updates the min_damage variable to be the minimum of the current min_damage and the calculated damage. This ensures that we keep track of the minimum damage across all shooting strategies.
# return min_damage

# Finally, the function returns the minimum damage calculated after evaluating all possible shooting strategies.
# input_str = input("Enter the number of soldiers on each consecutive aircraft: ")

# This line prompts the user to input the number of soldiers on each consecutive aircraft. The input is expected as a space-separated string.
# soldiers = list(map(int, input_str.split()))

# It converts the input string into a list of integers using the map function and split method. This list of integers represents the soldiers on each aircraft.
# result = minimum_damage(soldiers)

# The minimum_damage function is called with the soldiers list as an argument, and the result is stored in the variable result.
# print("Minimum amount of damage:", result)

# Finally, the code prints the minimum amount of damage to Ironman based on the shooting strategy and the input provided by the user.
# The code essentially considers each aircraft as the starting point for the shoot, calculates the damage caused by all other aircraft, and keeps track of the minimum damage encountered across all possible starting points.