def solution(scoville, K):
    answer = 0
    from heapq import heappush,heappop
    heap = []
    for sve in scoville:
        heappush(heap,sve)
    q = heappop(heap)
    while q < K:
        if len(heap) == 0:
            return -1
        q2 = heappop(heap)
        mixq = q + q2*2
        heappush(heap,mixq)
        q = heappop(heap)
        answer += 1
        
    
    return answer