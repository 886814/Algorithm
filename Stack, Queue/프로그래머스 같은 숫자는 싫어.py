def solution(arr):
    stack = [arr[0]]
    now = arr[0]
    for i in arr:
        if now != i:
            stack.append(i)
            now = i
    return stack