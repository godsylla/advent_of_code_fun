from itertools import combinations
import numpy as np


# write function to find the combination of strings that are only off by 1 letter
# that function should also return the index of the letter that's off
def one_letter_off_checker (string_a, string_b):
	''' we can assume that string_a and string_b have the same length'''

	off_counter = 0
	off_index = []

	for i in range(len(string_a)):
		if string_a[i] != string_b[i]:
			off_counter += 1
			off_index.append(i)
		else:
			pass

	return (off_counter, off_index)


def main ():
	# load in the inputs
	input_ = open('./dec_2_input.txt').read().split()

	# grab unique pair-wise combinations of all pssible inputs
	pairwise_combos = list(combinations(input_, 2))

	# run the checker on all input combos
	results = []
	for combo in pairwise_combos:
		results.append(one_letter_off_checker(combo[0], combo[1]))

	# find the index of which combo was only off by 1 letter:
	index = np.where([result[0] == 1 for result in results])[0][0]
	index_to_pop = results[index][1][0]
	
	# for the combo that's off by a letter,
	# pop out the letter that the 2 strings do not share in common
	temp_list = list(pairwise_combos[index][0])
	temp_list.pop(index_to_pop) # pop out the off-letter
	print(''.join(temp_list))


if __name__ == '__main__':
	main()




