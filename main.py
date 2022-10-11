
inputvalues = input('Enter all elements values: ')
numbers1 = inputvalues.split()
for i in range(len(numbers1)):
	numbers1[i] = int(numbers1[i]) 
evenlist = []

i=0
while numbers1 and i < len(numbers1):
	if int(numbers1[i]) % 2 == 0:
		evenlist.append(numbers1.pop(i))
		i-=1
	i+=1

print(numbers1)
print(evenlist)