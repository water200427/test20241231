def snake_matrix(n):
    result = []
    for i in range(n):
        for j in range(n - i):
            # print(f"{i=}, {j=}")
            # a_{i,0} = 1 + (1 + 2 + ... + i)
            # a_{i,0} = (i**2 + i + 2) // 2
            # a_{i,j} = a_{i,j-1} + (i + j + 1)
            # a_{i,j-1} = a_{i,j-2} + (i+ (j-1) + 1)

            # a_{i,j} = a_{i,0} + (i+2) + ... + (i+j+1)
            aij = (i**2 + i + 2) // 2 + (2 * i + j + 3) * (j) // 2
            # print(f"{aij}", end=" ")
            if j == n - i - 1:
                result.append(aij)
            else:
                result.append(str(aij) + " ")
        result.append("\n")
    print("".join(str(x) for x in result))


if __name__ == "__main__":
    snake_matrix(5)
# snake_matrix(5)
# 1 3 6 10 15
# 2 5 9 14
# 4 8 13
# 7 12
# 11
