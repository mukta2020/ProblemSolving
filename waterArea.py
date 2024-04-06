def waterArea(heights):
    maxHeight, pos = 0, 0
    area1, area2 = 0, 0
    if len(heights) == 0:
        return 0
    for i in range(len(heights)):
        if heights[i] > maxHeight:
            maxHeight = heights[i]
            pos = i
    if pos > 0:
        area1 = partOfArea(heights[: pos])
    if pos + 1 < len(heights):
        area2 = partOfArea(heights[pos+1:][::-1])
    return area1 + area2

def partOfArea(heights):
    lower = heights[0]
    area = 0
    for i in range(1, len(heights)):
        if heights[i] == 0:
            area += lower
        elif heights[i] < lower:
            area += lower - heights[i]
        elif heights[i] > lower:
            lower = heights[i]
    return area
print(waterArea([0, 0]))

#[0,8,0,0,5,0,0,10,0,0,1,1,0,3]