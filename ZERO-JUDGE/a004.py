data = []
while True:
    try:
        user = int(input())
        if user % 4 == 0 and user % 100 != 0:
            data.append("西元")
        else:
            data.append("閏年")
    except:
        break

for i in data:
    print(i)