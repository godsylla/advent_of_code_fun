from collections import Counter, defaultdict


# load input
input_ = open('./dec_2_input.txt').read().split()


# function to count for each string, how many letters appear > 1x
def doubles_triples_test (string_input):
    '''
    input is a string of alpha characters
    purpose is to count how often each of the letters repeat
    return how many letters appear twice
    return how many letters appear thrice
    as a tuple output: (count of letters appearing 2x, count of letters appearing 3x)'''
    
    counted_list_of_tuples = Counter(string_input).most_common()
    
    doubles_counter = 0
    triples_counter = 0
    
    for x in counted_list_of_tuples:
        if x[1] == 2:
            doubles_counter += 1
        elif x[1] == 3:
            triples_counter += 1
        else:
            pass
    
    return doubles_counter, triples_counter


# function to that fits the count criteria for the test
def aggregate_counter (double_triple_count):
    '''input is a tuple, index 0 with the double count, and index 1 with the triple count'''
    doubles_agg = 0
    triples_agg = 0
    
    if double_triple_count[0] != 0:
        doubles_agg += 1
    if double_triple_count[1] != 0:
        triples_agg += 1
    
    return doubles_agg, triples_agg


# RUN IT 
def main():
	input_ = open('./dec_2_input.txt').read().split()

	# create dict to store all ultimate counts
	ultimate_count_d = defaultdict(int)

	# check each input string
	for strings in input_:
		tup_count = doubles_triples_test(strings)
		tup_agg = aggregate_counter(tup_count)

		ultimate_count_d['double'] += tup_agg[0]
		ultimate_count_d['triple'] += tup_agg[1]

	print(ultimate_count_d['double'] * ultimate_count_d['triple'])


if __name__ == '__main__':
	main()

