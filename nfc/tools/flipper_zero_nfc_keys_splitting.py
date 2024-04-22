import os
import argparse, sys

parser=argparse.ArgumentParser()

parser.add_argument("--in", help="path for the NFC key file to split")
parser.add_argument("--out", help="path and name of file of results")

args=vars(parser.parse_args())



if len(args) > 0 :

	the_input_file = args.get('in')

	keys_for_splitting_file = open(the_input_file, 'r')
	lines = keys_for_splitting_file.readlines()

	count = 0
	count_no_duplicate = 0

	# Some info for file generated
	the_line_to_write = ['# Keys splitting with flipper_zero_nfc_keys_splitting.py\n# Author: inazo\n# GitHub: https://github.com/inaz0/flipperZero\n# Youtube Channel: https://www.youtube.com/@kanjian_fr/\n\n']

	# Parsing the lines

	for line in lines:
    		
		line = line.strip() + '\n'
		first_char_of_line = line[0]

		# if it's a comment we keep it in the file
		if first_char_of_line == '#' :
			the_line_to_write.append( line )
		else:
			# no difference for the flipper if line are uppercase or not
			line = line.upper()

			count += 1

			if line not in the_line_to_write :
				the_line_to_write.append( line )
				count_no_duplicate += 1

	  
	# Saving results
	output_result_file = open( args.get('out') , 'w') 
	output_result_file.writelines( the_line_to_write )
	output_result_file.close()
	

	print('Number of keys before splitting: ' + str(count))
	print('Number of keys after splitting: ' + str(count_no_duplicate))


