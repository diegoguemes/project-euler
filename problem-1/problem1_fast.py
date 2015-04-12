def sum_of_numbers_divisible_by(divisor, limit):
  N = (limit - 1) // divisor
  return N * (N + 1) / 2 * divisor

limit = 1000
total =  sum_of_numbers_divisible_by(3, limit) + \
         sum_of_numbers_divisible_by(5, limit) - \
         sum_of_numbers_divisible_by(15, limit)
print(total)