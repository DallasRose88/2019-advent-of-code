f = []
x = 0 
while x < len(f):
    if f[x] == 1:
        a = (f[x+1])
        b = f[x+2]
        c= f[x+3]
        d = f[a] + f[b]
        f[c] = d
        x += 4
        continue
    if f[x] == 2:
        a = (f[x+1])
        b = f[x+2]
        c= f[x+3]
        f[c] = (f[a]*f[b]) 
        x += 4 
        continue
    if f[x] == 99:
        break
print(f[0])
