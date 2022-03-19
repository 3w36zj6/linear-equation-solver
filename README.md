# linear-equation-solver
N次元の正方行列Aと列ベクトルB, Xについて、部分ピボット選択を用いたLU分解でAX=BをXについて解く。
## Requirements
- Python 3.9+

## Usage
#### Input
行列の成分は半角スペース区切り、Bは転置する。

```
N
A
B
```

### Example
#### Input

```
3
1 2 -4
2 3 7
3 5 2
-2 2 -1
```

#### Output

```
-16
9
1
```
