N = int(input())

input_d_list = []
for _ in range(N):

    d = int(input())
    input_d_list.append(d) 


d_list = [i for i in range(1,101)]

exsit_list = [0] * 100

for i in range(len(d_list)):

    for j in range(len(input_d_list)):

        if d_list[i] == input_d_list[j]:
            exsit_list[i] = 1


print(exsit_list.count(1))