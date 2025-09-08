def solve():
    # プラン数
    N = int(input())

    # 前回の時刻と座標を表す変数
    pt, px, py = 0, 0, 0

    # Nステップの移動をそれぞれ考える
    for i in range(N):
        # 移動先の情報を入力で受け取る
        t, x, y = map(int, input().split())

        # 前回の状態の差分をとる
        T, X, Y = t - pt, abs(x-px), abs(y-py)

        # 間に合わない場合は不可能
        if T < X + Y:
            return False
        
        # パリティが合わない時は不可能
        if T % 2 != (X + Y) % 2:
            return False
        
        # 前回情報を更新
        pt, px, py = t, x, y

    # 最後まで到達
    return True

print("Yes" if solve() else "No")