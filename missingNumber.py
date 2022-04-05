a = [1, 2, 3, 4, 6, 7, 8, 9, 10]

for i in range(1, 100):
    if i <= len(a) and (i != a[i-1]):
        print('Missing no is', i)
        break
