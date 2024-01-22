import sys
lines = [i.strip() for i in sys.stdin.readlines()]
M,N = map(int,lines[0].split())
check = {}
check[0] = 'WBWBWBWB'
check[1] = 'BWBWBWBW'
check['W'] = (check[0]+check[1])*4
check['B'] = (check[1]+check[0])*4
lines = lines[1:]
line_list = []
for line in lines:
    line_list.append(line)
chess_replace = []
loop_M = M - 8  
loop_N = N - 8
for k in range(loop_M + 1):
    for i in range(loop_N + 1):       
        total_word = ''
        for j in range(8):
            word = line_list[j+k][0+i:8+i]
            total_word += word
        check_black = 0
        check_white = 0
        for num in range(len(total_word)):
            if total_word[num] != check['B'][num]:
                check_black += 1
            if total_word[num] != check['W'][num]:
                check_white += 1
        chess_replace.append(check_black)
        chess_replace.append(check_white)
print(min(chess_replace))