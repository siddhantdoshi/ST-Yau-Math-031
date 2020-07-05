n = int(input("Enter 'N': "))

nacci_List = [0]
sub_List = []

counter = 0

while counter < n - 1:
		counter += 1
		nacci_List.append(0)
		sub_List.append(counter)

desired_Terms = int(input("How many terms?"))

times = n - 1
nacci_List[n - 1] = 1

while times != desired_Terms - 1:
		store = nacci_List[times]

		for x in sub_List:
			store = store + nacci_List[times - x]
		
		nacci_List.append(store)
		times += 1

print nacci_List[0:]