def largest_palindrome_product():
    largest = float('-inf')
    for a in reversed(range(100, 1000)):
        for b in reversed(range(100, 1000)):
            product = a * b
            if is_palindrome(product):
                largest = max(largest, product)
    return largest

def is_palindrome(number):
    return str(number) == str(number)[::-1]

print largest_palindrome_product()
