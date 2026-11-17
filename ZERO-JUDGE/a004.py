try:
    list1 = []
    while True:
        year = int(input())
        if year % 4 == 0 and year % 100 != 0:
            list1.append("閏年")
        if year % 400 == 0:
            list1.append("閏年")
        if year % 4 != 0:
            list1.append("平年")
        if year % 100 == 0 and year % 400 != 0:
            list1.append("平年")
except:
    for i in list1:
        print(i)