def max_natural_numbers_sum(S):
    left, right = 1, S
    
    while left <= right:
        mid = (left + right) // 2
        if mid * (mid + 1) // 2 <= S:
            left = mid + 1
        else:
            right = mid - 1
    
    return right

S = int(input())
print(max_natural_numbers_sum(S))