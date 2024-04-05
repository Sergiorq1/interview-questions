def list_sum(num_list):
  #base case: if list len equals 1,
  if len(num_list) == 1:
  # then return first index
    return num_list[0]
  #return first index plus list_sum(1:)
  return num_list[0] + list_sum(num_list[1:])
  # call stack:
  # first iteration: value of 1st index
  # second iteration: value of 1st, 2nd index
  # third iteration: value of 1st, 2nd, 3rd index 
  
print(list_sum([1,2,4,5,3,2,1]))
