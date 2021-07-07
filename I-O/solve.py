
#1
evens = [num for num in range(1,300) if num % 2 == 1]

#2

for num in evens :
	print(len(evens),num**2)


#3
print(57 in evens)