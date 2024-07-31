def solution(operations):
    answer = []
    from heapq import heappush,heappop,heapify
    heap = []

    def delMaxNum(heap):
        maxheap = list(map(lambda x:x*-1,heap))
        heapify(maxheap)
        heappop(maxheap)
        heap = list(map(lambda x:x*-1,maxheap))
        heapify(heap)
        return heap

    for opat in operations:
        cmd, num = opat.split(" ")
        num = int(num)
        if cmd == "I":
            heappush(heap,num)
        else:
            if len(heap) > 0:
                if num == -1:
                    heappop(heap)
                else:
                    heap = delMaxNum(heap)
    if len(heap) == 0:
        return [0,0]
    elif len(heap) == 1:
        lastheap = (heappop(heap))
        return [lastheap,lastheap]
    else:
        answer.append(heappop(heap))
        maxheap = list(map(lambda x:x*-1,heap))
        heapify(maxheap)
        answer.insert(0,-1*heappop(maxheap))

        return answer
    