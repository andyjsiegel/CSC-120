def sum_cols(grid: list[list[int]], n: int) -> int:
    if n > len(grid)+1:
        return 0
    return grid[0][n] + sum_cols(grid[1:], n)

# print(sum_cols([[1,2,3,4], [10,20,30,40], [100,200,300,400]], 2)) # 333

def replace(s: str, a: str, b: str) -> str:
    if not s:
        return ''
    else:
        if s[0] == a:
            return b + replace(s[1:], a, b)
        else:
            return s[0] + replace(s[1:], a, b)

# print(replace("banana", "a", "x"))

def replace2(s: str, a: str, b: str) -> str:
    if not s:
        return ''
    else:
        if s.startswith(a):
            return b + replace2(s[len(b):], a, b)
        return s[0] + replace2(s[1:], a, b)


print(replace2("banana", "an", "xD"))

def print_n(n: int) -> None: 
    if n == 0:
        return
    else:
        print_n(n-1)
        print(n)

def return_odd_positions(ints: list[int]) -> list[int]:
    if len(ints) < 2:
        return []
    return [ints[1]] + return_odd_positions(ints[2:])

# print(return_odd_positions([11, 22, 33, 44, 55])  )

def sum_list(integers: list[int]) -> int:
    if len(integers) < 2:
        return integers[-1]
    return integers[0] + sum_list(integers[1:])

print(sum_list([1,2,3,4,5]))