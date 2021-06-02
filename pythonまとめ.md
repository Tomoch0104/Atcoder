# pythonまとめ
pythonのクラス、メソッドに関してわからないことをまとめる

# zip()
- forループで複数のリストの要素を取得
- 要素数が異なる場合の処理
    - zip()関数では多い分の要素が無視される
    - itertools.zip_longest()関数では足りない部分の要素が埋められる
- 複数のイテラブルの要素をタプルにまとめたリストを取得


# numpy.where()
- Numpyで条件に応じた処理を行う
- np.where()を使うと、Numpy配列ndarrayに対して、条件を満たす要素を置換したり特定の処理を行ったりすることができる。条件を満たす要素のインデックス（位置）を取得することも可能
```python
import numpy as np

a = np.arange(9).reshape((3,3))
print(a)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

print(np.where(a < 4, -1, 100))
# [[ -1  -1  -1]
#  [ -1 100 100]
#  [100 100 100]]
```

- 条件を満たす場合は*True*、満たさない場合は*False*とするndarrayは、np.where()を使わずにndarrayを含む条件式で取得できる
```python
print(np.where(a < 4, True, False))
# [[ True  True  True]
#  [ True False False]
#  [False False False]]

print(a < 4)
# [[ True  True  True]
#  [ True False False]
#  [False False False]]
```

## 複数条件を適用
各条件式を()で囲み&や|を使うと、複数条件に対して処理が適用される。

```python
print(np.where((a > 2) & (a < 6>) , -1 , 100))
# [[100 100 100]
#  [ -1  -1  -1]
#  [100 100 100]]

print(np.where((a > 2) & (a < 6) | (a == 7), -1, 100))
# [[100 100 100]
#  [ -1  -1  -1]
#  [100  -1 100]]
```
- 複数条件の場合も、*True*、*False*のndarrayを取得するのはnp.where()を使わなくてもよい。
```python
print((a > 2) & (a < 6))
# [[False False False]
#  [ True  True  True]
#  [False False False]]

print((a > 2) & (a < 6) | (a == 7))
# [[False False False]
#  [ True  True  True]
#  [False  True False]]
```

## 条件を満たす要素を置換
- 条件を満たす場合も満たさない場合も任意の値に置換するのはこれまでの例の通り。
- 条件を満たす場合のみ、あるいは満たさない場合のみ任意の値に置換することもできる。
- np.where()の引数x,yに元のarrayを渡せば、元の値がそのまま使われる。
```python
print(np.where(a<4, -1, a))
# [[-1 -1 -1]
#  [-1  4  5]
#  [ 6  7  8]]

print(np.where(a<4, a, 100))
# [[  0   1   2]
#  [  3 100 100]
#  [100 100 100]]
```

- なお、np.where()は新たなndarrayを返し、元のndarrayは変更されない。

```python
a_org = np.arange(9).reshape((3,3))
prnt(a_org)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

a_new = np.where(a_org < 4, -1, a_org)
print(a_new)
# [[-1 -1 -1]
#  [-1  4  5]
#  [ 6  7  8]]

print(o_org)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]
```

- 元のndarray自体を更新したい場合は以下のような書き方ができる。
```python
a_org[a_org < 4] = -1
print(a_org)
# [[-1 -1 -1]
#  [-1  4  5]
#  [ 6  7  8]]
```

## 条件を満たす要素を処理
- 元のndarrayの値そのままではなく、演算した結果を使うこともできる。
```python
print(np.where(a < 4, a * 10, a))
# [[ 0 10 20]
#  [30  4  5]
#  [ 6  7  8]]
```

## 条件を満たす要素のインデックス（位置）を取得
- 引数x,yを省略した場合は、条件を満たす要素のインデックス（位置）を返す。

- 各次元（行、列など）に対して条件を満たすインデックス（行番号、列番号など）のndarrayのタプルとなる。

```python
print(np.where(a < 4))
# (array([0, 0, 0, 1]), array([0, 1, 2, 0]))

print(type(np.where(a < 4>)))
# <class 'tuple'>
```
- この場合、[0,0]、[0,1]、[0,2]、[1,0]の要素が条件をみたすという意味。

- 以下のようにlist()、zip()および*による要素の展開を組み合わせて各座標のリストを取得することも可能
```python
print(list(zip(*np.where(a < 4))))
# [(0, 0), (0, 1), (0, 2), (1, 0)]
```

- 三次元以上の多次元配列でも同様
```python
a_3d = np.arange(24).reshape(2, 3, 4)
print(a_3d)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
# 
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]

print(np.where(a_3d < 5))
# (array([0, 0, 0, 0, 0]), array([0, 0, 0, 0, 1]), array([0, 1, 2, 3, 0]))

print(list(zip(*np.where(a_3d < 5))))
# [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3), (0, 1, 0)]
```

- 一次元だということがわかっていれば、np.where()の結果の最初の要素をそのまま使ってもよい。この場合は要素数1個のタプルではなく整数intを要素とするndarrayとなる。リストに変換したい場合はtolist()。

```python
print(np.where(a_1d < 3)[0])
# [0 1 2]

print(np.where(a_1d < 3)[0].tolist())
# [0, 1, 2]
```