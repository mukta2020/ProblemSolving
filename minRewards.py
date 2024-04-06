def minRewards(scores):
    rewards = [1 for _ in scores]
    for i in range(1, len(scores)):
        if scores[i] > scores[i-1]:
            rewards[i] = rewards[i-1] + 1
    for i in reversed(range(len(scores) -1)):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)
    return sum(rewards)

def minRewards1(scores):
    minNumber = float("inf")
    reward = [1 for i in range(len(scores))]
    minPos = 0
    for i, s in enumerate(scores):
        if s < minNumber:
            minNumber = s
            minPos = i
    for i in range(minPos + 1, len(scores)):
        if scores[i-1] < scores[i]:
            reward[i] = reward[i - 1] + 1
        else:
            while i > minPos:
                if scores[i-1] > scores[i] and reward[i - 1] <= reward[i]:
                    reward[i - 1] += 1
                i -= 1
    for i in range(minPos-1, -1, -1):
        if scores[i+1] < scores[i]:
            reward[i] = reward[i + 1] + 1
        else:
            while i < minPos:
                if scores[i+1] > scores[i] and reward[i + 1] <= reward[i]:
                    reward[i + 1] += 1
                i += 1

    return sum(reward)

print(minRewards([2, 20, 13, 12, 11, 8, 4, 3, 1, 5, 6, 7, 9, 0]))