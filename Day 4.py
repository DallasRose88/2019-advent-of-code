total = 0 
x = 246515
while x < 739105:
    m = str(x)
    n = 0 
    count = 0
    good = 0 
    while n < 5:
        if m[n] == m[n+1]:
            count += 1 
        if m[n] <= m[n+1]:
            good += 1 
        n += 1 
    if count >= 1 and good == 5:
        total += 1 
    x += 1
print('part 1 =',total)
