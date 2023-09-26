def first_non_consecutive(arr):
  if not arr: return 0
  for i, x in enumerate(arr[:-1]:
    if x + 1 != arr[i+1]:
      return arr[i+1]

def basic_test_cases():
  test.assert_equals(first_non_consecutive([1,2,3,4,6,7,8], 6)
  test.assert_equals(first_non_consecutive([1,2,3,4,5,6,7,8], None)
  test.assert_equals(first_non_consecutive([-3,-2,0,1],0)
