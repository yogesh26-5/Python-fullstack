def divisors(n):
    a = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            a.append(i)
            if i != n // i:
                a.append(n // i)
    return sorted(a)
print(*divisors(36))