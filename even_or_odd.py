def even_or_odd(number):
  return 'Odd' if number % 2 else 'Even'

def basic_test_cases():
  test.assert_equals(even_or_odd(2), 'Even')
  test.assert_equals(even_or_odd(1), 'Odd')
  test.assert_equals(even_or_odd(0), 'Even')
  test.assert_equals(even_or_odd(15456452, 'Even')
  test.assert_equals(even_or_odd(-123), 'Odd')
