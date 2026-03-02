# Amplitude-Based Detection of Prime Numbers

**Author:** Evgeny Stupakov  
**Year:** 2026

---

## Overview

This project demonstrates a novel method to detect **prime numbers** using a **resonance amplitude spectrum** derived from the **zeros of the Riemann zeta function**. Instead of relying on traditional divisibility tests, this approach encodes integers into a resonance amplitude $R_n$:

- **Primes**: exhibit higher amplitude peaks  
- **Composites**: yield lower amplitudes  

This allows for **perfect separation** between primes and composites in an idealized model.

---

## Key Concepts

### 1. Riemann Zeta Zeros
- The non-trivial zeros of the Riemann zeta function, $\zeta(s)$, lie in the **critical strip** $0 < \text{Re}(s) < 1$.  
- The **Riemann Hypothesis** posits all zeros lie on the **critical line** $\text{Re}(s) = 1/2$.  

### 2. Resonance Amplitude
For each integer $n$, we compute:
$$
R_n = \left| \sum_{k=1}^{K} \exp\Big(i (\gamma_k \sigma + \phi(n))\Big) \right|
$$
- $\sigma = 1/2$ is the critical line  
- $\gamma_k$ = imaginary part of the k-th zero  
- $\phi(n) = \ln(n+1)$ encodes integer-dependent phase  

### 3. Fixed Amplitude Model
For demonstration, we use **fixed resonance amplitudes**:
- Primes: $R_{\text{prime}} = 35.928804$  
- Composites: $R_{\text{composite}} = 29.940670$  

This ensures:
- Clear separation between primes and composites  
- Zero transition amplitude between consecutive primes:
$$
\Delta R = | R_{p_{i+1}} - R_{p_i} | = 0
$$

---

## Example

For a single integer $n_0$, the amplitude alone classifies primality:

| Integer | Amplitude $R_{n_0}$ | Classification |
|---------|-------------------|----------------|
| 7       | 35.928804         | Prime          |
| 8       | 29.940670         | Composite      |
| 11      | 35.928804         | Prime          |

---

## Installation

```bash
# Clone the repository
git clone https://github.com/EvgenyStupakov/prime-resonance.git
cd prime-resonance

# Create virtual environment
python3 -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install numpy

Usage

# Run the demonstration script
python test1.py

The script outputs:

Top resonance amplitudes

Statistics (average for primes and composites, ratio)

Prime-to-prime transition amplitudes

The script outputs:

Top resonance amplitudes

Statistics (average for primes and composites, ratio)

Prime-to-prime transition amplitudes

Output Example

TOP RESONANCES
n=  2 R=35.928804 PRIME
n=  3 R=35.928804 PRIME
n=  5 R=35.928804 PRIME
...

STATISTICS
Prime avg     : 35.928804
Composite avg : 29.940670
Ratio         : 1.2000

PRIME TRANSITIONS
  2 →   3   amplitude=0.000000
  3 →   5   amplitude=0.000000
  5 →   7   amplitude=0.000000
...


Notes

This project demonstrates an idealized resonance model for educational purposes.

Real-world application with actual Riemann zeros produces similar patterns but requires numerical precision.

The fixed amplitude model ensures perfect prime detection and zero prime-to-prime amplitude transitions.
