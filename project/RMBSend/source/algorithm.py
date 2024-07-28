from configs import par
def calculate(m):#计算最少数量纸币的组合方法（贪心算法）
    res = []
    for p in par:
        if m >= p:
            res.append(m // p)
            m %= p
        else:
            res.append(0)
    return res
