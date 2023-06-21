Flag = True
while Flag:
    num = int(input())
    if num==0:
        Flag=False
    else:
        num = str(num)
        if num == num[::-1]:
            print('yes')
        else:
            print('no')
        