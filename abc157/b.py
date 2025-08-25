A = []

for i in range(3):

    row = list(map(int, input().split()))
    A.append(row)

N = int(input())

B = []
for i in range(N):
    
    b = int(input())
    B.append(b)

# print("A:", A)
# print("B:", B)

# 配列に含まれる数字のindexを行と列ごとにリストへ格納する
row_index_list = []
col_index_list = []
# B配列に登場するAの配列要素のindexを抽出する
for i in range(3):
    for j in range(3):
        for k in range(len(B)):

            if A[i][j] == B[k]:
                row_index_list.append(i)
                col_index_list.append(j)
                break

# print("row_index_list:", row_index_list)
# print("col_index_list:", col_index_list)

# ビンゴの判定
bingo = False

# 横が揃っている場合
if row_index_list.count(0) == 3 or row_index_list.count(1) == 3 or row_index_list.count(2) == 3:
    bingo = True

# 縦が揃っている場合
if col_index_list.count(0) == 3 or col_index_list.count(1) == 3 or col_index_list.count(2) == 3:
    bingo = True

#　斜めが揃っている場合
down_to_the_right_cnt = 0 # 右下がり斜め
up_to_the_right_cnt = 0 # 右上がり斜め
for i in range(len(row_index_list)):
        
    if row_index_list[i] == col_index_list[i]:
        down_to_the_right_cnt += 1

        if (row_index_list[i] == 1) and (col_index_list[i] == 1):
            up_to_the_right_cnt += 1
    
    if (row_index_list[i] == 2) and (col_index_list[i] == 0):
        up_to_the_right_cnt +=1
    
    if (row_index_list[i] == 0) and (col_index_list[i] == 2):
        up_to_the_right_cnt +=1

if (down_to_the_right_cnt == 3) or (up_to_the_right_cnt == 3):
    bingo = True

# 判定
if bingo: 
    print("Yes")
else: 
    print("No")

