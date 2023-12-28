def solution(bandage, health, attacks):
    attacks.sort(key=lambda x : x[0])
    max_health = health
    now, conti = 0, 0
    for attack in attacks:
        time, damage = attack
        for i in range(time - now - 1):
            health = min(health + bandage[1], max_health)
            conti += 1
            if conti == bandage[0]:
                health = min(health + bandage[2], max_health)
                conti = 0
        now = time
        health -= damage
        if health <= 0:
            return -1
        conti = 0
    return health
