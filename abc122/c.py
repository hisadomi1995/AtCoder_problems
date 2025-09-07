# 入力
N, Q = map(int, input().split())
S = input()

# 累積和csを求める
cs = [0]*(N+1)
for i in range(1, N):
    cs[i + 1] = cs[i] + (S[i - 1:i + 1] == "AC")

for q in range(Q):
    # 区間を取得
    l, r = map(int, input().split())

    # 右端に1を足して添字を0始まりにする
    l -= 1

    # 累積和を用いて答えを求める
    print(cs[r] - cs[l+1])
    