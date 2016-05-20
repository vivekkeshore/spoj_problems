# Vivek Keshore
# http://www.spoj.com/problems/COMDIV/

import sys
from fractions import gcd
from math import sqrt

def prime_sieve(num):
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

inputs = int(sys.stdin.readline())
for inp in xrange(inputs):
    d = sys.stdin.readline().split()
    x, y = int(d[0]), int(d[1])

    prime_nums = prime_sieve(max(x, y))

    # gcd_num = gcd(x, y)
    # gcd_sqrt = sqrt(gcd_num)
    #
    # for i in xrange(1, int(gcd_sqrt + 1)):
    #     if not gcd_num % i:
    #         v += 2
    #         if i == gcd_num/i:
    #             v -= 1
    #
    # sys.stdout.write(str(v) + '\n')

#
# gc=gcd(a,b);
# if(gc==1){
# printf(“1\n”);
# }
# else{
# i=0;
# an=1;
# while(gc && primes[i]<=gc && i<pind){
# c=0;
# while(gc%primes[i]==0){
# c++;
# gc/=primes[i];
# }
# an*=(c+1);
# i++;
# }
# if(gc>1)
# an<<=1;
# printf(“%d\n”,an);