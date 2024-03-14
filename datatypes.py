# creation of array
array1 = [1, 2, 3, "thimphu", 2.5]

# retrieving
element1 = array1[0]
element2 = array1[4]
lastElement = array1[-5]
#print(lastElement)

# modifying elements
# array1[0] = 10

# getting number of elements in an array
no_of_elements = len(array1)

# slicing
elements = array1[0:3]
#print(elements)

arr1 = [1,10]
arr2 = ['thimphu', 'wangdue']

number_to_check = 2
result = number_to_check in arr1
#print()

arr3 = arr2 + arr1
#print(arr3)

arrVariable = [1,3,2]
arrVariable.append(4) #[1,3,2,4]
print(arrVariable)

#insert at a specific index
arrVariable.insert(1,10)#[1,10,3,2,4]
arrVariable.sort()
print(arrVariable)

stackVar =[]
#adding to stack
stackVar.append(4)
stackVar.append(2)
stackVar.append(9)
stackVar.append(1)# 4,2,9,1
print('After appending', stackVar)
stackVar.pop()
print('After popping', stackVar)
print('removed elements:', elements)