def is_prime(func):
    def wrapper(*args):
        a = func(*args)
        b = 0
        for i in range(2, a):
            if a % i == 0:
                b += 1
        if b == 2:
            print('Составное')
        else:
            print('Простое')
        return a
    return wrapper

@is_prime
def sum_three(*args):
    sum_numbers = 0
    for i in args:
        sum_numbers += i
    return sum_numbers


result = sum_three(2, 3, 6)
print(result)
