with open('numbers.txt') as file:
	file_contents_as_list = file.readlines()
	# print file_contents_as_list;
	sum_per_line = [];
	for line in file_contents_as_list:
		# print line;
		sum_of_line = 0;
		for digit in line:
			# print digit;
			if digit.isdigit():
				sum_of_line+=int(digit)
		# print sum_of_line;
		sum_per_line.append(sum_of_line);
	# print sum_per_line;
	num_sum = (sum(sum_per_line));
	print num_sum;


