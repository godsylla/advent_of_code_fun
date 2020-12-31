def parse_input (filepath:str) -> list:
    with open (filepath, 'r') as f:
        return [l.strip() for l in f.readlines()]


def find_airplane_row (position_code:str) -> int:
    if len(position_code) != 10:
        raise ValueError ('Input must be length 10')
    
    front_back = position_code[:7]

    lower, upper = 0, 127
    for i, fb in enumerate(front_back):
        split = ((upper - lower) + 1) // 2 
        
        if front_back[i] == 'F':
            upper -= split 
        else:
            lower += split 
        
    if front_back[-1] == 'F': return min(lower, upper)
    else: return max(lower, upper)
    

def find_airplane_col (position_code:str) -> int: 
    if len(position_code) != 10:
        raise ValueError("Input must be length 10")
        
    left_right = position_code[7:]
    
    lower, upper = 0, 7
    for i, lr in enumerate(left_right):
        split = (upper - lower) // 2 + 1
        
        if left_right[i] == 'L':
            upper -= split
        else:
            lower += split
            
    if left_right[-1] == 'L': return min(lower, upper)
    else: return max(lower, upper)


if __name__ == '__main__':
    raw_lines = parse_input('./day5_part1_input.txt')
    
    seat_ids = list()

    for position in raw_lines: 
        row, col = find_airplane_row(position), find_airplane_col(position)
        seat_ids.append((row, col))
        
    print(max([(e[0] * 8) + e[1] for e in seat_ids]))
