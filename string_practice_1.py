"""
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26
统计字符串中每种字母的数量，忽略大小写
"""
def countchar(str):
    list = []
    a_list = [chr(i) for i in range(97, 123)]
    A_list = [chr(i) for i in range(65, 91)]
    i = 0
    while i < 26:
        list.append(0)
        i += 1
    for char in str:
        for j in range(0, 25):
            if char == a_list[j] or char == A_list[j]:
                list[j] += 1

    print(list)

countchar("aaAA")