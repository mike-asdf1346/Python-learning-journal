# a, b = input().split(" ")
# a = int(a)
# b = int(b)
# print(f"{a + b}")
data = input().split(' ')
convert = [int(i) for i in data]
result = sum(convert)
print(result)