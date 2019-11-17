terbesar = []
while True:
    n = int(input("masukan bilangan N: "))
    terbesar.append(n)
    if n == 0:
        break
print("nilai terbesar adalah : {}".format(max(terbesar)))
