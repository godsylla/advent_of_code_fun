import numpy as np 

# read in the input
# typically a txt file will return string types
input_ = open('./dec_1_input.txt').read().split()

# convert all the string types into integers
int_inputs = [int(x) for x in input_]

# use numpy to calculate the cumulative sum, and grab the last number in the returned array
def get_cum_sum (list_of_ints):
	cumsum = np.cumsum(list_of_ints)
	last_dig = cumsum[-1]
	return last_dig

## RUN IT 
def main():
	input_ = open('./dec_1_input.txt').read().split()

	int_inputs = [int(x) for x in input_]

	print(get_cum_sum(int_inputs))


if __name__ == '__main__':
	main()