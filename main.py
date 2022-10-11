
inputvalues = input('Enter all elements values: ')
numbers = inputvalues.split()
for i in range(len(numbers)):
	numbers[i] = int(numbers[i]) 
evenlist = []

i=0
while numbers and i < len(numbers):
	evenlist.append(numbers.pop(i))
	i+=1

print("The list numbers ", numbers)
print("The list for even index elements", evenlist)