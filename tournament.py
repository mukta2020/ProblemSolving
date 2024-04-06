def tournamentWinner(competitions, results):
    d = {}
    for i in range(len(results)):
        if results[i] == 0:
            if competitions[i][1] not in d:
                d[competitions[i][1]] = 3
            else:
                d[competitions[i][1]] += 3
        elif results[i] == 1:
            if competitions[i][0] not in d:
                d[competitions[i][0]] = 3
            else:
                d[competitions[i][0]] += 3
    maxValue = -1
    winner = ""
    for k, v in d.items():
        if v > maxValue:
            maxValue = v
            winner = k
    return winner
competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
    ]
results = [0,0,1]

print(tournamentWinner(competitions, results))