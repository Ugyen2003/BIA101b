

# input array
arr = [3,4,5,6,7,8,9]
target = 7

low = 0
high = len(arr) - 1

# loop
result = False
while low < high:
    # divide
    mid = (low + high) // 2 # this is the middle index (not the value of the arr)
    
    # compare the midddle with the target 
    if arr[mid] == target:
     print('found')
     break

    # compare the discard the half
    if target > arr[mid]:
        low = mid + 1
    else:
      high = mid - 1
      
if result == True:
    print('found')
    
else:
    print('not found')