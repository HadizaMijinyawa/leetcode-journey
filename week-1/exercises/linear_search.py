#############
### LINEAR SEARCH has a time complexity of
### O(n)
#############


def linear_search(list, key):

   """
   LINEAR SEARCH

   Function that accepts a list and a number to search for (key), loops through a list, if key is found return the index of the else return none
   """

   for i in range(0, len(list)):
      if(list[i] == key):
         print(f"{list[i]} found at index {i}")
         return i
   return -1


def verify(index):
   if(index < 0):
      print("item not found")

## Testing
numbers=[1,2,3,4,6,9]
result= linear_search(numbers, 5)
verify (result)

## Testing
numbers=[1,2,3,4,6,9]
result= linear_search(numbers, 2)
verify (result)
