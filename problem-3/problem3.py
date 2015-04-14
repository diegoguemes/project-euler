def largest_prime_factor(N):
    largest = 2
    number = N
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            largest = divisor
            number /= divisor
        divisor += 1
    return largest

print largest_prime_factor(600851475143)