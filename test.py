def multiply_setup(a: int) -> callable:
    def multiply(b: int) -> int:
        return a * b
    return multiply

def exponential_setup(power: float) -> callable:
    def exponentiate(base: float) -> float:
        return base**power
    return exponentiate

sqrt = exponential_setup(0.5)
cbrt = exponential_setup(0.333333333333333333)
print(sqrt(4))
print(cbrt(64))
