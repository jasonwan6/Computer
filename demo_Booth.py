def getcplmt(st, f = 0):  # 获取补码
    s = st.copy()
    flag = s[0]
    s.reverse()
    i = s.index('1') + 1
    if (flag is '-'):
        for t in s[i:]:
            if (t is '1'):
                s[i] = '0'
            elif (t is '0'):
                s[i] = '1'
            else:
                s[i] = t
            i += 1
        s.reverse()
        s.remove('-')
        s.insert(0, '1')
        if (f != 0):
            s.insert(0, '1')
    else:
        s.reverse()
        s.insert(0, '0')
        if (f != 0):
            s.insert(0, '0')
    return s


def get_x(xt): #返回 - B补码


    x = xt.copy()
    if (x[0] is '-'):
        x.remove('-')
        return getcplmt(x, 1)
    else:
        x.insert(0, '-')
        return getcplmt(x, 1)


def format(st):  # 先格式化数据，除去前面的零  方便代码实现
    s = st.copy()
    i = 0
    if (s[0] is '-'):
        i = 1
    while (s[i] is '0'):
        s.remove('0')
    return s


def add(A, B):  # 二进制相加
    A = A.copy()
    B = B.copy()
    i = len(B) - 1
    d = 0  # 进位
    while (i >= 0):
        if (A[i] is '0' and B[i] is '0'):
            if (d == 0):
                A[i] = '0'
            else:
                A[i] = '1'
                d = 0
        elif (A[i] is '1' and B[i] is '1'):
            if (d == 0):
                A[i] = '0'
            else:
                A[i] = '1'
            d = 1
        else:
            if (d == 0):
                A[i] = '1'
            else:
                A[i] = '0'
                d = 1
        i -= 1
    return A


def coculate(X, _X, Y):
    B = X.copy()
    _B = _X.copy()
    C = Y.copy()
    if ('.' in X):
        B.remove('.')
        _B.remove('.')
    A = ['0' for i in B]
    if ('.' in C):
        C.remove('.')
    C.append('0')
    i = len(C) - 2
    Cn = []
    re = []

    while (i >= 0):
        if (C[i] is '1' and C[i + 1] is '0'):
            Cn.append('-')
        elif (C[i] is '0' and C[i + 1] is '1'):
            Cn.append('+')
        else:
            Cn.append('0')
        i -= 1
    l = len(Cn) - 1
    i = 0
    for t in Cn:
        if (t is '+'):
            A = add(A, B)
        elif (t is '-'):
            A = add(A, _B)
        if (l != i):
            re.insert(0, A.pop())
            if (A[0] is '1'):
                A.insert(0, '1')
            else:
                A.insert(0, '0')
        i += 1
    A.extend(re)
    return A


def main():
    xt, yt = input("请输入乘数被乘数 空格隔开").split()
    x = format(list(xt))
    y = format(list(yt))
    X = getcplmt(x, 1)
    _X = get_x(x)
    Y = getcplmt(y)
    print("X补:", ''.join(X), " -X补:", ''.join(_X), " Y补:", ''.join(Y))
    re = []
    point = 0
    if ('.' in X):
        point = X.index('.')
        re = coculate(X, _X, Y)
        re.insert(point, '.')
    else:
        re = coculate(X, _X, Y)
    print("结果：", ''.join(re[1:]))


if __name__ == "__main__":
    main()
