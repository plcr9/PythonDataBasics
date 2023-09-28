def digits(number):
  return len(str(number))

def example_tests():
  test.assert_equals(digits(5),1)
  test.assert_equals(digits(12345),5)
  test.assert_equals(digits(9876543210),10)
