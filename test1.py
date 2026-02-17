import math
import cmath


FROM = 1
TO = 1000      

K_MAX = 200       
sigma = 0.5
threshold = 0.2

zeros = [
    14.134725, 21.022040, 25.010858, 30.424876,
    32.935062, 37.586178, 40.918719, 43.327073,
    48.005150, 49.773832
]


def von_mangoldt(n):

    if n < 2:
        return 0

    temp = n
    p = 2

    while p * p <= temp:

        power = 0

        while temp % p == 0:
            temp //= p
            power += 1

        if power > 0:
            return math.log(p)

        p += 1

    if temp > 1:
        return math.log(temp)

    return 0



def is_prime(n):

    if n < 2:
        return False

    for i in range(2, int(math.isqrt(n)) + 1):

        if n % i == 0:
            return False

    return True



def resonance(n):

    total = 0+0j

    for t in zeros:

        s = complex(sigma, t)

        for k in range(1, K_MAX+1):

            Λ = von_mangoldt(k)

            if Λ == 0:
                continue

            total += Λ / (k**s) * cmath.exp(1j * n * math.log(k))

    return abs(total)



resonant = []
true_primes = []

for n in range(FROM, TO+1):

    R = resonance(n)

    if R > threshold:
        resonant.append(n)

    if is_prime(n):
        true_primes.append(n)


correct = [n for n in resonant if is_prime(n)]
false = [n for n in resonant if not is_prime(n)]



print(f"Диапазон проверки: {FROM} → {TO}")
print(f"Глубина оператора: {K_MAX}")
print()

print("Настоящие простые:")
print(true_primes)

print("\nРезонансные числа:")
print(resonant)

print("\nПравильно обнаруженные простые:")
print(correct)

print("\nЛожные резонансы:")
print(false)

print("\nAccuracy:",
      len(correct),
      "/",
      len(resonant) if resonant else 1)

