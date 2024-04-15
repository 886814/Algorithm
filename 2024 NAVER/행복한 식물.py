emotions = [2,1,3,4,3]
orders = [2,2,2,2,5,5,5]
new_emotions = emotions
result = []
for order in orders:
    new_emotions = [x-1 for x in new_emotions]
    if new_emotions[order-1] >= 0:
        new_emotions[order-1] = emotions[order-1]
    result.append(len([x for x in new_emotions if x > 0]))

print(result)
