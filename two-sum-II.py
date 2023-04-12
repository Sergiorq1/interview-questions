# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

def twoSum(numbers: list[int], target: int):
    # Notes
    # Brute force soluton Time complexity of O(n^2):
        # check each individual combination by running a for loop inside a for loop 
    #test input:

    # [1,4,5,7,9,13,23,25,30]

    # Pointer Solution time complexity O(n)
    #Declare a left and right pointer
    left_pointer = 0
    right_pointer = len(numbers) -1
    # while solution isn't found
    while numbers[left_pointer] + numbers[right_pointer]!=target:
        # solution equals two pointer elements added togethr
        solution = numbers[left_pointer] + numbers[right_pointer]  
        # if solution is greater than target
        if solution > target:
            #move right pointer down one
            right_pointer-=1
        #if solution is less than target
        else:
            #move left pointer up one
            left_pointer+=1 
    #runs after solution is found
    return [left_pointer + 1 , right_pointer + 1]

print(twoSum([1,4,5,7,9,13,23,25,30], 30))