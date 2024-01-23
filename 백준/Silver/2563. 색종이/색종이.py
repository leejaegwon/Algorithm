import sys

Map = [[0 for j in range(100)] for i in range(100)]
papers = [list(map(int,data.split())) for data in sys.stdin.readlines()]
for paper in papers[1:]:
    W = paper[0]
    H = paper[1]
    for j in range(10):
        for k in range(10):
            Map[W+j][H+k] = 1
area = sum([sum(i) for i in Map])
print(area)
