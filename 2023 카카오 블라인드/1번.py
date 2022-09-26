def time(s):
    temp = list(map(int,s.split(".")))
    year = (temp[0]-2000)*12*28
    month = temp[1] * 28
    print(year + month + temp[-1])
    return year + month + temp[-1]

ans = []
today = "2020.01.01"
terms = ["Z 3", "D 5"]
terms_new = {}
for term in terms:
    x,y = term.split()
    terms_new[x]=int(y)

privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D","2019.07.01 D", "2018.12.28 Z"]
today = time(today)
    
new_ = [time(privacy.split()[0]) + terms_new[privacy.split()[1]]*28 for privacy in privacies]
for i in range(len(new_)):
    if new_[i] <= today:
        ans.append(i+1)
