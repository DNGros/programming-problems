import sys

# read in all the data
data = map(int,sys.stdin.read().splitlines())

# find the largest N I'm going to have to solve for
largestTest = max(data[1:])

# sieve of greek dude to find the primes up that
isPrime = [True]*largestTest
isPrime[0] = isPrime[1] = False

primes = []

for i, ep, in enumerate(isPrime):
    if ep:
        primes.append(i)
        for makePrime in xrange(i*i, largestTest, i):
            isPrime[makePrime] = False

# now handle test cases
for case in data[1:]:
    s = 0
    for n in xrange(2, case):
        for prime in primes:
            if n % prime == 0 :
                s += 1
            if prime > n:
                break
    print s
