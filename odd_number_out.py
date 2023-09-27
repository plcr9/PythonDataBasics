from collections import Counter

def stray(arr):
  result = 0
  for num in arr:
    result ^= num
  return result

def basic_test_cases():
  test.assert_equals(stray([1,1,1,1,1,1,2],2)
  test.assert_equals(stray([2,3,2,2,2],3)
  test.assert_equals(stray([3,2,2,2,2],3)
