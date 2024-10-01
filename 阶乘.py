def jc(num: int) -> int:
    if num == 0:
        return 1
    else:
        return num * jc(num - 1)


print(jc(3))
