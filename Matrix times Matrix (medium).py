def matrixmul(a:list[list[int|float]], b:list[list[int|float]])-> list[list[int|float]]: 
    x, y = len(a), len(b[0])
    if len(a[0]) != len(b):
        return -1
    c = [[0 for i in range(y)] for j in range(x)]
    for i in range(x):
        for j in range(y):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    return c

if __name__=="__main__":
    a = [[1, 2], [3, 4]]
    b = [[2, 1], [3, 4]]
    print(matrixmul(a, b)) # output:[[8, 9], [16, 18]]