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
