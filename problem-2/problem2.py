def fibonacci(N):
    sum = 0
    fn_1 = 1
    fn_2 = 1
    fn = 1
    while fn < N:
        if fn % 2 == 0:
            sum += fn
        fn = fn_1 + fn_2
        fn_2 = fn_1
        fn_1 = fn
    return sum

print fibonacci(4000000)