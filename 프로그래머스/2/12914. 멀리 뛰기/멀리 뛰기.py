def solution(n):
    answer = 0
    data = {}
    data[1] = 1
    data[2] = 2
    x = 3
    while x <= n:
        data[x] = data[x-1] + data[x-2]
        x += 1
    answer = data[n] % 1234567
    
    return answer