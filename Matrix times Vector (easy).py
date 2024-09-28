def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    c = []
    for i in range(len(a)):
        sum = 0
        if len(a[i]) != len(b):
            return -1
        for j in range(len(b)):
            sum += a[i][j]*b[j]
        c.append(sum)
    return c

if __name__ == "__main__":
    a = [[1,2],[2,4]]
    b = [1,2]
    print(matrix_dot_vector(a,b)) # [5, 10] 