def prise_summary():
    count = input()
    data = []
    for _ in range(int(count)):
        row = input()
        data.append(row.split(" "))
    print(data)


if __name__ == "__main__":
    prise_summary()
## input
# 4
# YaoLin 87 82 Y N 0
# ChenRuiyi 88 78 N Y 1
# LiXin 92 88 N N 0
# ZhangQin 83 87 Y N 1

## output
# ChenRuiyi
# 9000
# 28700
