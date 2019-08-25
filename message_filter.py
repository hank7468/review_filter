all_data = [] # Collect all data in this list
i = 0 # i = data counts
with open('reviews.txt', 'r') as f:
	for line in f:
		all_data.append(line.strip())
		i += 1
		if i % 1000 == 0:
			print(i)

filtered_data = []
for line in all_data: # "line" is only used in current for loop.
	if len(line) <= 100:
		filtered_data.append(line.strip())
print('there are', len(filtered_data), 'datas with less than or equal to 100 characters.')

good_data = []
for line in all_data:
	if 'good' in line:
		good_data.append(line.strip())
print('there are', len(good_data), 'datas mention "good".')