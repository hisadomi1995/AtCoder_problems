# 優先度付きキューのアルゴリズムでも解けそう
# 参考 : https://qiita.com/uniTM/items/9630ed9d51f62b3e35ab
# 袋の中を表現するリスト
ball_list = []

# クエリを順番に処理する。
Q = int(input())
for _ in range(Q):
  # クエリ取得
  query = list(map(int, input().split()))
  match query:
    case [1, x]:
      # 袋に入れる
      ball_list.append(x)
    case [2]:
      # 最小値を取得する。
      mi = min(ball_list)
      # 最小値を出力する。
      print(mi)
      # 最小値を一つ袋から消す。
      ball_list.remove(mi)