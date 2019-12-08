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

# Once done processing, step forward 4 positions

