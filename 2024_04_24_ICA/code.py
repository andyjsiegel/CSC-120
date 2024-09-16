# def fun1(x):
#     return 1/x

# def fun2(x):
#     try:
#         value = 1 + fun1(x)
#     except:
#         value = ''
#     return value 

# def main():

#     z = fun2(3)
#     print(z)
#     z = fun2(0)
#     print(z)

# main()

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Example usage
# number = 16
# if is_power_of_two(number):
#     print(f"{number} is a power of 2")
# else:
#     print(f"{number} is not a power of 2")

def print_pwrs_of_two(n):
    boolean = n > 0 and (n & (n - 1)) == 0
    for i in range(0,n):
        if 2**i > n and not boolean:
            break
        else:
            print(2**i)

print_pwrs_of_two(4)