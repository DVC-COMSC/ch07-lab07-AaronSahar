
inputvalues = input('Enter all elements values: ')
numbers1 = inputvalues.split() 
evenlist = []
i=0
while numbers1 and i < len(numbers1):
	if int(numbers1[i]) % 2 == 0:
		evenlist.append(numbers1.pop(i))
		i-=1
	i+=1

print("The list numbers ", numbers1)
print("The list for even index elements", evenlist)

# ******************************
# Make your Code
# ******************************
