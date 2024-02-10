import sys
lines = [i.strip() for i in sys.stdin.readlines()]
N = int(lines[0])
lines = lines[1:]
# arr_word = []
# arr_word = [[j for j in i] for i in lines]
arr_word = lines
max_words = []

def get_long_aph(arr_words:list):
    for words in arr_words:
        word_list = []
        cur_word = ''
        for aph in words:
            if cur_word == aph:
                word_list[-1] += 1
            else:
                word_list.append(1)
                cur_word = aph
    for i in range(len(arr_words)):
        cur_word = ''
        words = [word[i] for word in arr_words]
        for aph in words:
            if cur_word == aph:
                word_list[-1] += 1
            else:
                word_list.append(1)
                cur_word = aph
    return max(word_list)

max_words.append(get_long_aph(arr_word))
for i in range(N):
    for j in range(N-1):
        cur_arr = [[j for j in i] for i in lines]
        cur_arr[i][j], cur_arr[i][j+1] = cur_arr[i][j+1],cur_arr[i][j]
        max_words.append(get_long_aph(cur_arr))
    for j in range(N-1):
        cur_arr = [[word[i] for word in arr_word] for i in range(N)]
        cur_arr[i][j], cur_arr[i][j+1] = cur_arr[i][j+1],cur_arr[i][j]
        max_words.append(get_long_aph(cur_arr))
print(max(max_words))