"""
莫尼森数m
满足m=2**p-1且m和p均为素数
找出前5个莫尼森数

我的思路：
1.首先得到素数列表
2.假设这个数为m，即使莫尼森数
3.判断p是否在素数列表中（这一步可以改成直接判断p是否为素数） 后来我改成括号里的方法了
    p=log(m+1)/log(2)
"""

from math import sqrt, log


def prime(num):
    # 判断number是否是素数，是的话返回True
    tmp = int(sqrt(num))
    i = 2
    if num == 1:
        return False
    elif num == 2 or num == 3:
        return True
    elif num % 6 == 1 or num % 6 == 5:
        while i <= tmp:
            if num % i == 0:
                return False
            i += 1
        return True
    else:
        return False


def monisen():
    prime_list = []
    monisen_list = []
    p_list = []
    i = 2
    while i < 500000:
        if prime(i):
            prime_list.append(i)
        i += 1
    print(prime_list)

    for number in prime_list:
        j = log(number + 1) / log(2)
        if prime(j):
            monisen_list.append(number)
            p_list.append(int(j))
    print(monisen_list)


monisen()
