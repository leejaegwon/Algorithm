N = input().strip()
lenN = (len(N))
number = int(N)
digits = 0
while lenN > 0:
    cur_digit_num = 10**(lenN-1)
    digits += (number - cur_digit_num + 1) * (lenN)
    number = cur_digit_num-1
    lenN -= 1
print(digits)
