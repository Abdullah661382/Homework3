def Formula1(a, b, c):
    d = (b**2) - (4*a*c)
    return (- b + d**0.5)/(2*a)


def Formula2(a, b, c):
    e = (b**2) - (4*a*c)
    return (- b - e**0.5)/(2*a)


print(Formula1(1, 2, -3))
print(Formula2(4, 5, -6))
