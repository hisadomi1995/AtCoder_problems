N = int(input())

# 入力した文字列のリスト
s_list = []
for _ in range(N):

    input_str = input()
    s_list.append(input_str)

# アルファベットの文字の各文字の出現回数のリスト
alphabet_appear_cnt_list = [0] * 26

# アルファベットの小文字のリスト
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', \
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', \
                 'u', 'v', 'w', 'x', 'y', 'z']

all_s_alphabet_apper_cnt_list = []

for i in range(len(s_list)):

    s = s_list[i]
    for j in range(10):

        for k in range(len(alphabet_list)):
            
            if alphabet_list[k] == s[j]:
                alphabet_appear_cnt_list[k] += 1
    
    all_s_alphabet_apper_cnt_list.append(alphabet_appear_cnt_list)
    alphabet_appear_cnt_list = [0] * 26


# アナグラムということは、アルファベットの文字の出現回数が同じ
corresponding_cnt = 0
for i in range(len(all_s_alphabet_apper_cnt_list)):

    for j in range(i+1, len(all_s_alphabet_apper_cnt_list)):

        if all_s_alphabet_apper_cnt_list[i] == all_s_alphabet_apper_cnt_list[j]:
            corresponding_cnt += 1
    

print(corresponding_cnt)




