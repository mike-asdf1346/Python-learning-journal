n = 10 # how deep the pyramid is 
for i in range(1, n + 1):
    for j in range(n - i, 0, -1):
        print(" ", end="")
    for a in range(0, (2 * i - 1)):
        print("*", end="")

    print("")