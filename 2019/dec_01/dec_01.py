# PART 1: To Find the Fuel Required for a Module
    # mass / 3 
    # round down
    # subtract 2
# Find Fuel Requirements for ALL of the modules on your spacecraft

# PART 2: Recalculating fuel requirements
# That take into account the mass of the added fuel
    #  Treat each calculated fuel requirement for each module
    #  as input fuel for the subsequent module

import math 

# Note: Run from the dec_01/ file directory
# Note that the input for Part1 and Part2 are the same
with open ('./dec_01_input_a.txt', 'r') as f1:
    modules = f1.readlines()
    modules = [int(mod) for mod in modules]

def main_part1():
    # Calculate Fuel Requirements per Module
    fuel_reqd = [math.floor(mod/3)-2 for mod in modules]
    print(sum(fuel_reqd))

def calc_fuel_req (module:int) -> int:
    '''
    Keep calculating the fuel requirement 
    '''
    assert module > 0, 'No fuel required'

    fuel_start = module
    fuel_reqs = []
    while fuel_start > 0:
        fuel_end = math.floor(fuel_start/3)-2

        if fuel_end > 0:
            fuel_start = fuel_end
            fuel_reqs.append(fuel_end)
        else:
            break

    return sum(fuel_reqs) 

def main_part2(modules_l:list) -> list:
    '''
    Take a list of modules and calculate the fuel requirements
    '''
    fuel_reqs = [calc_fuel_req(mod) for mod in modules]
    print(sum(fuel_reqs))


if __name__ == '__main__':
    main_part1()
    main_part2(modules)