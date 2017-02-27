def is_prime(n):
    if n < 2:
        return False
    divisors = 0
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            divisors += 1
    return divisors == 1

def primes(n):
    numbers = [i for i in range(0, n+1)]
    for number in numbers:
        if number != -1 and is_prime(number):
            temp_num = number
            while temp_num + number < n:
                temp_num += number
                numbers[temp_num] = -1
    #print(numbers)
    return [prime for prime in numbers if prime != -1 and prime >= 2]

p = primes(3*10**5)