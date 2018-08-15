g = (x * x for x in range(10))
for n in g:
    print(n)

print("======triangles0======")
rows = 10
i0 = 0
result = []
while i0 < rows:
    number = 1
    j0 = 0
    row = []
    while j0 <= i0:
        row.append(int(number))
        number = number * (i0 - j0) / (j0 + 1)
        j0 = j0 + 1
    print(row)
    i0 = i0 + 1


def triangles():
    num = 1
    i = 0
    j = 0
    rowNums = []
    while j <= i:
        if j == i:
            rowNums.append(int(num))
            result = rowNums

            # 每次yield时重置参数  start
            j = 0
            i = i + 1
            rowNums = []
            num = 1
            # 每次yield时重置参数  end

            yield result
        else:
            rowNums.append(int(num))
            num = num * (i - j) / (j + 1)
            j = j + 1


print("======triangles======")
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
