def bin2dec(n: int):
    x, j = 0, 0
    while n > 0:
        x += (n % 10) * 2 ** j
        n //= 10
        j += 1
    return x

print(bin2dec(1101))
print(int("1101", 2))

