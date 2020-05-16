import time


def check_win_three(x):
    return x == "111" or x == "000"


def check_win_nine(x):
    if check_win_three(x[:3]):
        return True
    if check_win_three(x[3:6]):
        return True
    if check_win_three(x[6:]):
        return True

    if check_win_three(x[0] + x[3] + x[6]):
        return True
    if check_win_three(x[1] + x[4] + x[7]):
        return True
    if check_win_three(x[2] + x[5] + x[8]):
        return True

    if check_win_three(x[0] + x[4] + x[8]):
        return True
    return check_win_three(x[2] + x[4] + x[6])


def check_win_27(x):
    if check_win_nine(x[:9]):
        return True
    if check_win_nine(x[9:18]):
        return True
    if check_win_nine(x[18:]):
        return True

    if check_win_nine(x[:3] + x[9:12] + x[18:21]):
        return True
    if check_win_nine(x[3:6] + x[12:15] + x[21:24]):
        return True
    if check_win_nine(x[6:9] + x[15:18] + x[24:]):
        return True

    front, in_between, back = "", "", ""

    for i in range(0, 25, 3):
        front += x[i]
        in_between += x[i+1]
        back += x[i+2]

    if check_win_nine(front):
        return True
    if check_win_nine(in_between):
        return True
    if check_win_nine(back):
        return True

    if check_win_three(x[0] + x[13] + x[26]):
        return True
    if check_win_three(x[2] + x[13] + x[24]):
        return True
    if check_win_three(x[6] + x[13] + x[20]):
        return True
    if check_win_three(x[8] + x[13] + x[18]):
        return True

    return false


def brute_check_tictactoe():
    for i in range(pow(2, 27)):
        option = "{0:b}".format(i).zfill(27)
        if option[:9].count('1') == 5 and option.count('1') == 14:
            if not check_win_27(option):
                print(option)
                break


start = time.time()
brute_check_tictactoe()
end = time.time()
print(end - start)
print("no tie possible!")