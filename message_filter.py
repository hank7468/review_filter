data = []
num_character = input('please enter the maximum characters number used in the review: ')
num_character = int(num_character)
with open('reviews.txt', 'r') as f:
	for message in f:
		if len(message) < num_character:
			print(message)
			print('------------------------------------------------------')
			data.append(message.strip())
print('there are', len(data), 'reviews which is less than', num_character, 'characters.')