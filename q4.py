def criteria_loop(n, k):
    loop = [n % (10**k)]
    for i in range(2, 10000):
        # print(f"{loop=}")
        r = pow(n, i, 10**k)
        if r in loop:
            print(i - 1)
            return
        else:
            loop.append(r)

    print(-1)
    return


if __name__ == "__main__":
    criteria_loop(32, 2)

# criteria_loop(123, 3)
