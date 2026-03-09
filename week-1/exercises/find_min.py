def find_min(numbers):
   """
   Takes a list of numbers
   and returns the minimum number
   """

   min = numbers [0]
   for n in numbers :
      if n < min :
         min = n
         #print(min, n)
   return min


#Test
num_list = [5,2,8,1,9]
min_num = find_min(num_list)
print(f"The minimum number in {num_list} is {min_num}")
