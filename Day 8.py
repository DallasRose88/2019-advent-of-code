f = ''
layers = (len(f)//25)//6
numInLayer = (len(f))//layers
pixels = {}
zeros = []
x = 0
while x < layers:
    pixels[x] = []
    count = 0
    one = 0
    two = 0 
    y = x * layers 
    end = y + numInLayer
    while y < end:
        if int(f[y]) == 0:
            count += 1 
        if int(f[y]) == 1:
            one += 1
        if int(f[y]) == 2:
            two += 1 
        y += 1 
    zeros.append(count)
    pixels[x].append(one*two)
    #pixels[x].append(two)
    x += 1
smallest = min(zeros)
index = zeros.index(smallest)
print(pixels[index])
