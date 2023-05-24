competitions1 = [["HTML", "C#"],["C#", "Python"],["Python", "HTML"]]
results  = [0,0,1]

scores = {}

def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] +=points

for idx, competitions in enumerate(competitions1):
    result = results[idx]
    competitions.pop(result)

    for i in competitions:
        updateScores(i, 3, scores)


resulys_new = max(scores, key=scores.get)

resulys_new



