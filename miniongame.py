def minion_game(string):
    # your code goes here
    vowels='AEIOU'
    kev_scr= 0
    stu_scr = 0
    length = len(string)
    for i in range(length):
        if string[i] in vowels:
            kev_scr += length-i
        else:
            stu_scr += length-i        
    if kev_scr > stu_scr:
        print("Kevin", kev_scr)
    elif kev_scr < stu_scr:
        print("Stuart", stu_scr)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)
    