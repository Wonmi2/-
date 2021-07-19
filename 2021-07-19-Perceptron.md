# 퍼셉트론의 개념

퍼셉트론은 신경망(딥러닝)의 기원이 되는 알고리즘이다.

'인공뉴런'의 의미로 사용할 퍼셉트론은 다수의 신호를 입력으로 받아 하나의 신호를 출력한다.

신호를 받을 때에는 신호에 각각의 가중치가 곱해지고, 뉴런에서 이 신호의 총합이 정해진 한계를 넘을 때 뉴런이 활성화된다. 
= 1을 출력한다.

가중치가 클수록 해당 신호(특성)이 더 중요하다는 것을 나타낸다.

## y = { 0 (x1w1 +x2w2 =< theta), 1 (x1w1 + x2w2 > theta)

# 단순한 논리회로

## AND 게이트 (0,0,0,1)
```python
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7    
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
    
print(AND(0, 0)) # 0 을 출력
print(AND(0, 1)) # 0 을 출력
print(AND(1, 0)) # 0 을 출력
print(AND(1, 1)) # 1 을 출력
```

    0
    0
    0
    1
    

```python
def AND(x1, x2):
    w1, w2, b = 0.5, 0.5, -0.7    
    tmp = x1*w1 + x2*w2 + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1
    
print(AND(0, 0)) # 0 을 출력
print(AND(0, 1)) # 0 을 출력
print(AND(1, 0)) # 0 을 출력
print(AND(1, 1)) # 1 을 출력
```

    0
    0
    0
    1
    


```python
import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    for xs in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        y = AND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
```

    (0, 0) -> 0
    (0, 1) -> 0
    (1, 0) -> 0
    (1, 1) -> 1
    

## NAND 게이트 (1,1,1,0)
```python
import numpy as np


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    for xs in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        y = NAND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
```

    (0, 0) -> 1
    (0, 1) -> 1
    (1, 0) -> 1
    (1, 1) -> 0
    

## OR 게이트 (0,1,1,1)
```python
import numpy as np


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    for xs in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        y = OR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
```

    (0, 0) -> 0
    (0, 1) -> 1
    (1, 0) -> 1
    (1, 1) -> 1
    

## XOR 게이트 (0,1,1,0)
```python
from and_gate import AND
from or_gate import OR
from nand_gate import NAND


def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

if __name__ == '__main__':
    for xs in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        y = XOR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
```

    (0, 0) -> 0
    (0, 1) -> 1
    (1, 0) -> 1
    (1, 1) -> 0

