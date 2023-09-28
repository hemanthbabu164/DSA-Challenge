def sieve_eratosthenes(end):
    is_prime = [True] * (end + 1)
    is_prime[0] = is_prime[1] = False  
    p = 2
    while p * p <= end:
        if is_prime[p]:
            for i in range(p * p, end + 1, p):
                is_prime[i] = False
        p += 1
    primes = [i for i in range(2, end + 1) if is_prime[i]]
    return primes

def find_primes_in_range(start, end):
    primes = sieve_eratosthenes(end)
    return [prime for prime in primes if prime >= start]


print(find_primes_in_range(1, 10)) 
print(find_primes_in_range(20, 40)) 
print(find_primes_in_range(50, 60))  

'''
Time Complexity: O(N log log N)
Space Complexity: O(N)

'''
