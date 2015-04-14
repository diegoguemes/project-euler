def largest_palindrome_product():
    largest = float('-inf')
    for half in reversed(range(100, 998)):
        palindrome = make_palindrome_from(half)
        for divisor in reversed(range(100, 999)):
            if palindrome % divisor == 0 and palindrome // divisor <= 999:
                return palindrome
    return largest

def make_palindrome_from(half):
    return int(str(half) + str(half)[::-1])

print largest_palindrome_product()

