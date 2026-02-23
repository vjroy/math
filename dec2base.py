def bin2dec(n: int) -> int:
    neg = False
    if n < 0:
        n *= -1
        neg = True
    x, j = 0, 0
    while n > 0:
        bit = n % 10
        if bit != 0 and bit != 1:
            raise ValueError("Input contains digits other than 0 and 1")
        x += (bit) * 2 ** j
        n //= 10
        j += 1
    if neg:
        x *= -1
        return x
    return x

def dec2bin(n: int) -> str:
    if n == 0:
        return "0"
    neg = False
    if n < 0:
        n *= -1
        neg = True
    stack = []
    x = ""
    while n >= 1:
        stack.append(n % 2)
        n //= 2
    while stack:
        x += str(stack.pop())
    if neg:
        return "-" + x
    return x

print(bin2dec(-1101))
print(dec2bin(-13))
print(bin2dec(int(dec2bin(-13))))
print(dec2bin(bin2dec(-1101)))
#print(bin2dec(-1234))
