def solution(plans):
    stack,ans = [], []
    for plan in plans:
        name, start, playtime = plan
        hour, minute = map(int,start.split(":"))
        time = hour*60 + minute
        plan[1] = time
        plan[2] = int(playtime)

    plans.sort(key=lambda x : x[1])

    for i in range(len(plans)-1):
        name, start, playtime = plans[i]
        now = start + playtime
        if now <= plans[i+1][1]:
            remainder = plans[i+1][1] - now
            ans.append(name)
            while stack:
                if stack[-1][-1] < remainder:
                    remainder -= stack[-1][-1]
                    ans.append(stack.pop()[0])
                else:
                    stack[-1][-1] -= remainder
                    if stack[-1][-1] == 0:
                        ans.append(stack.pop()[0])
                    break
        else:
            remainder = now - plans[i+1][1]
            stack.append([name, remainder])
    else:
        ans.append(plans.pop()[0])
        while stack:
            ans.append(stack.pop()[0])
    return ans