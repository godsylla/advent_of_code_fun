from icecream import ic

# Part 1
def count_increases (depths: list):
    incr_count = 0

    for i in range(1, len(depths)):
        if depths[i] > depths[i-1]:
            incr_count += 1
        else:
            pass

    return incr_count


# Part 2
def count_k_window_increases (depths: list):
    incr_counter = 0 

    for i in range(len(depths)-3):
        ays = depths[i: i+3]
        bes = depths[i+1: i+4]
        
        if sum(ays) < sum(bes):
            incr_counter += 1
    
    return incr_counter        
    

if __name__ == '__main__':

    # Input
    with open('./01-12-2021_input.txt', 'r') as f:
        parsed_lines = f.readlines()
    depths = [int(num.strip('\n')) for num in parsed_lines]

    # Part 1
    ic(count_increases(depths))

    # Part 2
    ic(count_k_window_increases(depths))