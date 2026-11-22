# My-Python-Learning-Journey

## a) 项目简介

这是一个 Python 初学者练习仓库，目前包含两个小工具：

1. **猜数字游戏**：程序随机生成一个 1~100 的整数，玩家不断输入猜测，程序提示“太大/太小”，直到猜中为止，并统计一共猜了几次。
2. **BMI 计算器**：根据传入的姓名、体重（kg）和身高（m）计算 BMI 值，并判断体重属于“过轻 / 正常 / 过重 / 肥胖”哪个区间。

这两个程序分别练习了 **循环 + 条件判断 + 随机数** 和 **函数定义 + 参数传递 + 多分支判断**，是 Python 基础语法的入门练习。

## b) 文件说明

| 文件名 | 用途 |
|---|---|
| `猜数字.py` | 猜数字游戏。运行后程序随机生成 1~100 的整数，玩家反复输入猜测，程序给出大小提示并统计猜测次数。 |
| `bmi1.py` | BMI 计算器。定义 `fun_bmi(person, weight, height)` 函数，计算并打印 BMI 值及体重区间。 |

> 注意：`bmi1.py` 只定义了函数，**直接运行不会输出任何内容**，需要在文件末尾添加调用，或在交互式环境中调用，具体见“运行方式”。

## c) 代码说明

### 1. 猜数字游戏 `猜数字.py`

核心流程：

- 使用 `random.randint(1, 100)` 生成 1~100 的随机整数作为答案；
- 用 `count = 0` 记录猜测次数；
- 用 `while True` 循环让玩家反复猜，每猜一次 `count += 1`；
- 用 `if / elif / else` 判断猜测值与答案的大小关系：
  - 小于答案：提示“太小了，再大一点”；
  - 大于答案：提示“太大了，再小一点”；
  - 等于答案：用 f-string 输出答案和猜测次数，然后 `break` 退出循环。

关键代码：

```python
import random

secret = random.randint(1, 100)
count = 0

while True:
    guess = int(input("请输入你的猜测（1-100中的整数）："))
    count += 1

    if guess < secret:
        print("太小了，再大一点！")
    elif guess > secret:
        print("太大了，再小一点！")
    else:
        print(f"猜对了！答案就是 {secret}，你一共猜了 {count} 次。")
        break
```

已知限制：输入非整数（如字母）时，`int()` 会抛出 `ValueError` 导致程序退出。后续可以加入 `try / except` 处理。

### 2. BMI 计算器 `bmi1.py`

核心流程：

- 定义函数 `fun_bmi(person, weight, height)`，接收姓名、体重、身高三个参数；
- 先用字符串拼接打印个人信息；
- 用公式 `bmi = weight / (height * height)` 计算 BMI；
- 用 `if / elif / else` 按 BMI 区间输出结果：
  - `<= 18.5`：体重过轻
  - `18.5 ~ 24.9`：正常范围
  - `24.9 ~ 29.9`：体重过重
  - 其他：肥胖

关键代码：

```python
def fun_bmi(person, weight, height):
    print(person + '的身高：' + str(height) + 'm,体重为：' + str(weight), 'kg')
    bmi = weight / (height * height)

    if bmi <= 18.5:
        print('你的bmi为：' + str(bmi) + '体重过轻')
    elif bmi >= 18.5 and bmi < 24.9:
        print('你的bmi为：' + str(bmi) + '正常范围')
    elif bmi >= 24.9 and bmi < 29.9:
        print('你的bmi为：' + str(bmi) + '体重过重')
    else:
        print('你的bmi为：' + str(bmi) + '肥胖')
```

说明：当前区间在边界值（如 18.5、24.9）上存在重叠，实际运行时由于 `if / elif` 按顺序匹配，会归入前一个区间。后续可以统一边界写法，例如把“过轻”改成 `< 18.5`，让区间不重叠。

## 运行方式

### 猜数字游戏

在终端中执行：

```bash
python 猜数字.py
```

按提示输入 1~100 的整数即可开始游戏。

### BMI 计算器

`bmi1.py` 只定义了函数，直接运行不会输出。有两种使用方式：

**方式一**：在文件末尾添加调用代码，然后运行：

```python
fun_bmi('小明', 70, 1.75)
```

```bash
python bmi1.py
```

**方式二**：在 Python 交互式环境或 Jupyter Notebook 中导入后调用：

```python
from bmi1 import fun_bmi
fun_bmi('小明', 70, 1.75)
```

输出示例：

```
小明的身高：1.75m,体重为：70 kg
你的bmi为：22.857142857142858正常范围
```

## 学习收获

通过这两个小练习，练习了：

- 变量、字符串拼接与 f-string 格式化
- `input()` 输入与 `int()` 类型转换
- `if / elif / else` 多分支条件判断
- `while` 循环与 `break`
- `random` 模块生成随机数
- 函数定义、参数传递与函数调用
- 边界值处理与区间判断的基本思路
