K = int(input())
A, B = list(map(int, input().split()))

IsAchievable = False

for dst in range(A, B+1):

    if dst % K == 0:
        IsAchievable = True
        break

if IsAchievable:
    print('OK')

else:
    print('NG')