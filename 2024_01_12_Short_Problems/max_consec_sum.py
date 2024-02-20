def max_consec_sum(numbers, n):
    # n is the number of consecutive numbers to add
    max_sum = sum(numbers[0:n])  # max_sum is the sum of the first n elements (for 2 this is the sum of the first two elements, exclusive)
    for index in range(n, len(numbers)): # starts at n and ends at the final element of the list ie max_consec_sum([10,2,-3,4,3],2) goes from 2-5
        print(index-n, index) # for 2 this is every combination of length 2 (0,2) (1,3) (2,4)
        window_sum = sum(numbers[index-n:index]) # Calculate the sum of that combination
        if window_sum > max_sum:  # Compare the sum of the current window with the maximum sum so far
            max_sum = window_sum  # Update max_sum if necessary
    return max_sum



print(max_consec_sum([10,2,-3,4,3],1)) 
# 10

print(max_consec_sum([10,2,-3,4,3],2))
# 12

print(max_consec_sum([10,2,-3,4,3],3))
# 9

print(max_consec_sum([10,2,-3,4,3],4))
# 13

print(max_consec_sum([10,2,-3,4,3],5))
# 16