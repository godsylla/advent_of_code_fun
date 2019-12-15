## NOTE
# 99 means that the program is finished and should immediately halt
# opcodes are comprised of natural numbers 1 (min) and 99 (max)

# opcode: 1
    # adds numbers read from two positions
    # stores the sum in a 3rd position
# opcode: 2
    # multiplies two inputs
    # stores the product in a 3rd position

# the first integer is the position
# three integers immediately AFTER the opcode tells you the 3 pos'ns
    # 1st & 2nd: positions from which you should read input values
    # 3rd: position at which output should be stored

# Once done processing, step forward 4 positions to reach next opcode

# BEFORE BEGINNING
# a) replace position 1 with the value 12
# b) replace position 2 with the value 2

# REFERENCED: https://dev.to/jbristow/advent-of-code-2019-solution-megathread-day-2-1202-program-alarm-31jk
# for help

def process_opcodes (num_array:list, num1=12, num2=2) -> int:
    '''
    Before beginning, replace pos 1 with 12 and pos 2 with 2.
    Val 1 = value at the index num_array[1]
    Val 2 = value at the index num_array[2]
    '''
    num_array[1] = num1
    num_array[2] = num2

    i = 0
    while num_array[i] != 99:
        opcode = num_array[i]
        val1 = num_array[num_array[i + 1]]
        val2 = num_array[num_array[i + 2]]
        idx3 = num_array[i + 3]
        # opcode = 1
        if opcode == 1:
            num_array[idx3] = val1 + val2
        # opcode = 2
        elif opcode == 2:
            num_array[idx3] = val1 * val2
        i += 4
    
    return num_array[0]

def main ():
    with open ('./dec_02_inputA.txt') as f:
        for line in f:
            gravity = [int(g) for g in line.split(',')]
    
    # Part 1
    print(process_opcodes(gravity))
     

if __name__ == '__main__':
    with open ('./dec_02_inputA.txt') as f:
        for line in f:
            gravity = [int(g) for g in line.split(',')]

    # Part 1
    main()

    # Part 2 
    GOAL = 19690720
    
    for i in range(100):
        for j in range(100):
            if process_opcodes(gravity[:], i, j) == GOAL:
                print(100 * i + j)
                break

