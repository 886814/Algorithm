alp = 0
cop = 0
problems = [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]
max_al, max_co = 0, 0
dp = [[100000] * (155) for _ in range(155)]
for problem in problems:
    al,co,_,_,_ = problem
    if al > max_al:
        max_al = al
    if co > max_co:
        max_co = co
alp = min(alp, max_al)
cop = min(cop, max_co)
dp[alp][cop] = 0
for i in range(alp,max_al+1):
    for j in range(cop,max_co+1):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
        dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
        for problem in problems:
            alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
            if  i >= alp_req and j >= cop_req:
                alp_ = min(i+alp_rwd, max_al)
                cop_ = min(j+cop_rwd, max_co)
                dp[alp_][cop_] = min(dp[alp_][cop_], dp[i][j]+cost)
print(dp[max_al][max_co])