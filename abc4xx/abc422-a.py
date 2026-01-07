s = list(i for i in input())

if int(s[2]) < 8:
    j = int(s[2]) + 1
    print(s[0] + "-" + str(j))
elif int(s[2]) == 8:
    i = int(s[0]) + 1
    print(str(i) + "-" + "1")
