def solution(cards1, cards2, goal):
    answer = 'Yes'
    from collections import deque

    q1 = deque()
    for _ in cards1:
        q1.append(_)
    q2 = deque()
    for _ in cards2:
        q2.append(_)

    for word in goal:

        if len(q1) > 0 and word == q1[0]:
            q1.popleft()
        elif len(q2) > 0 and word == q2[0]:
            q2.popleft()
        else:
            return "No"
    return answer