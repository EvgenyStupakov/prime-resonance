
import numpy as np
import matplotlib.pyplot as plt
r_zero_re = 0.5
r_zeros_im = np.array([
    14.134725141, 21.022039639, 25.010857580, 30.424876125, 32.935061588,
    37.586178159, 40.918719012, 43.327073281, 48.005150881, 49.773832478,
    52.970321478, 56.446247697, 59.347044003, 60.831778525, 65.112544048,
    67.079810529, 69.546401711, 72.067157674, 75.704690699, 77.144840069,
    79.337375020, 82.910380854, 84.735492980, 87.425274613, 88.809111208,
    92.491899270, 94.651344041, 95.870634228, 98.831194218, 101.317851006,
    103.725538040, 105.446623052, 107.168611184, 111.029535543, 111.874659177,
    114.319365906, 116.226680321, 118.790782865, 121.370125002, 122.946829294,
    124.256818554, 127.516683879, 129.578704194, 131.087688537, 133.497737638,
    134.756509753, 137.215193831, 139.736208952, 141.123707523, 143.111845330
])

def von_mangoldt(n):
    if n < 2:
        return 0
    for p in range(2, int(n**0.5)+1):
        if n % p == 0:
            k = 0
            m = n
            while m % p == 0:
                m //= p
                k += 1
            if m == 1:
                return np.log(p)
            else:
                return 0
    return np.log(n)

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

N = 10000
numbers = np.arange(1, N+1)
prime_mask = np.array([is_prime(n) for n in numbers])

def phi_div(n):
    return sum(1/d for d in range(2, n) if n % d == 0)

def R(n, zeros_im, sigma):
    base_phase = sigma * np.sqrt(n) * zeros_im + np.log(n+1)
    signal = (von_mangoldt(n)+1) * np.sum(np.exp(1j*(base_phase + phi_div(n))))
    return np.abs(signal)

resonances = np.array([R(n, r_zeros_im, r_zero_re) for n in numbers])

print("n   R(n)       * если простое")
for n, r, prime in zip(numbers, resonances, prime_mask):
    mark = "*" if prime else " "
    print(f"{n:3d} {r:10.6f} {mark}")

prime_avg = resonances[prime_mask].mean()
comp_avg = resonances[~prime_mask].mean()
ratio = prime_avg / comp_avg

print(f"\nСредний резонанс простых   : {prime_avg:.6f}")
print(f"Средний резонанс составных : {comp_avg:.6f}")
print(f"Соотношение prime/composite: {ratio:.4f}")


plt.figure(figsize=(12,6))
plt.plot(numbers, resonances, color='gray', label='R(n)')
plt.scatter(numbers[prime_mask], resonances[prime_mask], color='red', s=10, label='primes')
plt.xlabel('n')
plt.ylabel('|R(n)|')
plt.title('Resonance Amplitudes of Integers up to N')
plt.legend()
plt.tight_layout()
plt.savefig("resonance_spectrum.png")
plt.close()
