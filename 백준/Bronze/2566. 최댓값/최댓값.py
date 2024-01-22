import sys
Matrix = [list(map(int,data.split())) for data in sys.stdin.readlines()]
maxnum = 0
maxrow = 0
maxcol = 0

for i,Mat_row in enumerate(Matrix):
    #line = list(map(int,input().split()))
    for j in range(len(Mat_row)):
        if maxnum <= Mat_row[j]:
            maxnum = Mat_row[j]
            maxrow = i
            maxcol = j
print(maxnum)
print(maxrow+1,maxcol+1)