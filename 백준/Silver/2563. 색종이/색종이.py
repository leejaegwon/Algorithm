import sys
count = int(sys.stdin.readline())
Matrix=[]
for i in range(100):
    Matrix.append([])
    for j in range(100):
        Matrix[i].append(False)

for i in range(count):
    N,M = map(int,sys.stdin.readline().split())
    N = N - 1
    M = M - 1 
    for i in range(N,N+10):
        for j in range(M,M+10):
            Matrix[i][j] = True
block = 0
for i in range(len(Matrix)):
    for j in range(len(Matrix[i])):
        if Matrix[i][j] == True:
            block += 1
print(block)
