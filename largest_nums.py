# Given an array a of n numbers and a count k find the k largest values in the array a.
# Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  ⇒  [6, 8, 7]

#O(log(n)) time complexity solution
def largest_nums(nums:list, k:int):
  #sort array
  nums.sort()
  #if k is larger than length of list or less than 1, return error 
  if k > len(nums) or k < 1:
    return -1
  # return the largest numbers from end of list
  return nums[-k:]

print(largest_nums([1,4,5,6,2,7,3,2,78], 4))

# Another solution with O(n) time complexity solution
def largest_nums_n(nums:list, k:int):
  pass
  # declare variable largest_nums that is a list 
  largest_nums = []
  # and takes in k number of elements
  # Iterate through list 
  for index in range(len(nums)):
    if len(largest_nums) == k:
      # check if index is larger than smallest number in largest_nums
      if nums[index] > largest_nums[0]:
        largest_nums.pop(0)
        largest_nums.append(nums[index])
        largest_nums.sort()
    else:
      largest_nums.append(nums[index])
  return largest_nums


print(largest_nums_n([1,4,5,6,2,7,3,2,78], 4))