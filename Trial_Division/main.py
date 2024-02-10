#Ακολουθώ πιστά τον αλγόριθμο που μου δίνετε από το textbook
N = 2**62 - 1
#N = 2**102 - 1

L = []  #Is the list that we shall add all the divisors of n.
while N % 2 == 0:
    L.append(2)
    N = N // 2
f = 3  #A possible divisor of n, also called trial divisor.
while f ** 2 <= N:
    if N % f == 0:
        L.append(f)
        N = N // f
    else:
        f = f + 2
if (N != 1):
    L.append(N)

print(L)