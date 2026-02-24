A = {1, 2, 3, 4, 5}
B = {0, 2, 4} #Python seperates sets because there is no key:value 

C = set()

x = [1, 1, 1, 1, 2, 2, 3]
print(list(set(x)))
print(f"A | B: {A | B}")
print(f"A & B: {A & B}")
print(f"A - B: {A - B}")
print(f"A ^ B: {A ^ B}")