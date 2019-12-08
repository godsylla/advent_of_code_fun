# PART 1: To Find the Fuel Required for a Module
    # mass / 3 
    # round down
    # subtract 2
# Find Fuel Requirements for ALL of the modules on your spacecraft


import math 

# Note: Run from the dec_01/ file directory
with open ('./dec_01_input.txt', 'r') as f:
    modules = f.readlines()
    modules = [int(mod) for mod in modules]

def main_part1():
    # Calculate Fuel Requirements per Module
    fuel_reqd = [math.floor(mod/3)-2 for mod in modules]
    print(sum(fuel_reqd))

if __name__ == '__main__':
    main_part1()