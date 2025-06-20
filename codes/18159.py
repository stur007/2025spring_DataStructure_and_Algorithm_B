def euler_sieve():
    primes = [True]*10002
    primes[0] = False
    primes[1] = False
    for i in range(2, 10002):
        if primes[i]:
            for j in range(2, 10002):
                if j*i <10001:
                    primes[i*j] =False
                else:
                    break
    true_primes = []
    for i in range(len(primes)):
        if primes[i]:
            true_primes.append(i)
    return true_primes
t =  int(input())
true_primes = euler_sieve()
for i in range(t):
    print(f'Case{i+1}:')
    n = int(input())
    ans = []
    for primes in true_primes:
        if primes < n:
            if primes%10 ==1:
                ans.append(primes)
        else:
            break
    if ans:
        print(*ans)
    else:
        print('NULL')
