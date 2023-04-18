# Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
# Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  t=20  ⇒  [13, 6] or [4, 17] or [5, 14]

# O(n) time complexity
def closest_nums(nums1, nums2, t):
  ##Two pointer approach
  #sort both lists
  nums1.sort()
  nums2.sort()
  #declare closest to infinite value 
  closest = float('inf')
  # declare closest pair to none
  closest_pair = None
  #first pointer that starts from the beginning of first array 
  start_1 = 0
  #second pointer that starts from the end of the second array
  end_2 = len(nums2)-1
  #while both pointers have not traversed the ends of their lists
  while start_1 < len(nums1) and end_2 >= 0:
    # the sum of both pointers, this changes every loop
    sum_pointers = nums1[start_1] + nums2[end_2]
    #if the difference of the newly declared sum of pointers is less then the current 
    #closest
    if abs(sum_pointers - t) < abs(closest - t):
      #the new closest is assigned to the current sum of pointers
      closest = sum_pointers
      # the closest pair is updated to the two pointers 
      closest_pair = (nums1[start_1], nums2[end_2])
    #if the current sum of pointers is less than target value,
    if sum_pointers < t:
      #the first pointer goes up one element
      start_1 += 1
    #if the current sum of pointers is greater than or equal to the target value,
    else:
      #the second pointer goes down one element 
      end_2 -= 1
  # return the closest pair
  return list(closest_pair)

print(closest_nums([9, 13, 1, 8, 12, 4, 0, 5],[3, 17, 4, 14, 6],20))