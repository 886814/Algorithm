N = int(input())
stack = []
queue = [(i+1, int(x)) for i, x in enumerate(input().split())]
index = 0

while len(queue) > 1:
    former = stack.pop() if stack else (0, 0)
    current = queue[index]
    next_ = queue[index + 1] if index < len(queue) - 1 else (0, 0)

    if former[1] <= current[1] and next_[1] <= current[1]:
        stack.append((current[0], former[1] + current[1] + next_[1]))
        index += 2
    elif former[1] <= current[1]:
        stack.append((current[0], former[1] + current[1]))
        index += 1
    elif next_[1] <= current[1]:
        stack.append(former)
        stack.append((current[0], next_[1] + current[1]))
        index += 2
    else:
        stack.append(former)
        stack.append(current)
        index += 1

    if index >= len(queue):
        index = 0
        queue, stack = stack, []

print(f"{queue[0][1]}\n{queue[0][0]}")