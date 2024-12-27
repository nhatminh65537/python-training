def gcd(a: int, b: int) -> int:
    while a % b != 0:
        a, b = b, a % b
    return b

def legendre(a: int, p: int) -> int:
    return pow(a, (p-1)//2, p)

def lcm(a: int, b: int) -> int:
    return a*b // gcd(a, b)