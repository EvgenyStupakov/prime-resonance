import numpy as np
N = 1000
critical_amplitude = 35.928804
composite_amplitude = 29.940670

numbers = np.arange(1, N+1)
def is_prime(n):
    if n < 2: 
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: 
            return False
    return True

prime_mask = np.array([is_prime(n) for n in numbers])

resonances = np.full_like(numbers, composite_amplitude, dtype=float)
resonances[prime_mask] = critical_amplitude

prime_indices = np.where(prime_mask)[0]
prime_transitions = []
for i in range(len(prime_indices)-1):
    p_idx = prime_indices[i]
    q_idx = prime_indices[i+1]
    amp_diff = abs(resonances[q_idx] - resonances[p_idx])
    prime_transitions.append((numbers[p_idx], numbers[q_idx], amp_diff))

prime_avg = resonances[prime_mask].mean()
comp_avg = resonances[~prime_mask].mean()
ratio = prime_avg / comp_avg

print("TOP RESONANCES")
top_indices = np.argsort(-resonances)[:30]
for idx in top_indices:
    typ = "PRIME" if prime_mask[idx] else "composite"
    print(f"n={numbers[idx]:3d} R={resonances[idx]:.6f} {typ}")

print("\nSTATISTICS")
print(f"Prime avg     : {prime_avg:.6f}")
print(f"Composite avg : {comp_avg:.6f}")
print(f"Ratio         : {ratio:.4f}")

print("\n PRIME TRANSITIONS")
for p, q, amp in prime_transitions:
    print(f"{p:3d} → {q:3d}   amplitude={amp:.6f}")
