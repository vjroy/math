def bin2dec(n: int):
    x, j = 0, 0
    while n > 0:
        x += (n % 10) * 2 ** j
        n //= 10
        j += 1
    return x

def dec2bin(n: int):
    stack = []
    x = ""
    while n >= 1:
        stack.append(n % 2)
        n //= 2
    while stack:
        x += str(stack.pop())
    return int(x)
print(bin2dec(dec2bin(13)))

