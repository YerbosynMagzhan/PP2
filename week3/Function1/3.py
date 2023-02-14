def solve(numheads, numlegs):
    extra_legs = numlegs - 2 * numheads
    rabbits = extra_legs / 2 
    chicken = numheads - rabbits
    print("Chicken: ", chicken , " ", "Rabbits: ", rabbits)
    
heads = int(input())
legs = int(input())
animals = solve(heads, legs)

