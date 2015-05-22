# Vivek Keshore
# http://www.spoj.com/problems/PRIME1/

from math import sqrt


def prime_list(num):
    prime_bool = [True] * 100001
    prime_range = int(sqrt(num))
    prime_nums = []

    k = int(sqrt(prime_range))
    for i in xrange(2, k+1):
        if prime_bool[i]:
            for j in xrange(i*i, prime_range+1, i):
                prime_bool[j] = False

    for i in xrange(2, prime_range+1):
        if prime_bool[i]:
            prime_nums.append(i)

    return prime_nums

if __name__ == "__main__":
    inp = int(raw_input())
    for i in xrange(inp):
        x = (raw_input().split())
        m, n = int(x[0]), int(x[1])

        try:
            prime_nums = prime_list(n)
        except:
            pass
        prime_bool = [True] * 100001

        for prime_num in prime_nums:
            sieve = m / prime_num
            sieve *= prime_num

            for j in xrange(sieve, n+1, prime_num):
                if j >= m:
                    prime_bool[j-m] = False

        for prime_num in prime_nums:
            if prime_num >= m and prime_num <= n:
                print prime_num

        for i in xrange(n-m+1):
            if prime_bool[i] and (i + m != 1):
                print i+m
        print ''
