tuple_1 = ("a", "b", "c", "d")
tuple_2 = (1, 1, 3, 4, 5, 6, 1, 1, 1, 1)

result = list(tuple_1[::2] + tuple_2[1::2])
result = set(result)
print(result)