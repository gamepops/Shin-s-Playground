# receive user input
intList = input('pls input a list of integers')
tupleList = {} # restore matched integers
# iterate the input integers
for i in intList:
	for j in intList:
		if i == j: # ignore same integers
			continue
		# even product or odd sum
		if ((i * j) % 2 == 0) or ((i + j) % 2 == 1):
			tupleList.append((i, j))
# print the matched pair
print('pairs list:')
for t in tupleList:
	print(t[0], ', ', t[1])
