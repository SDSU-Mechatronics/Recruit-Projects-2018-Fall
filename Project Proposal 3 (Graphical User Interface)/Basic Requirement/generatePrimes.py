
primes = [2, 3]

for i in range(2, 10000):
	isPrime = True
	for p in primes:
		if i % p == 0:
			isPrime = False
	
	if isPrime:
		primes.append(i)
		print i
