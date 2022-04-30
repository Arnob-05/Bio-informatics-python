
# calculateing GC content

gene = open("brca1_bap1.txt", "r")

# skip the header
gene.readline()

g = 0
a = 0
c = 0
t = 0

for line in gene:
    line = line.lower()
    for char in line:
        if char == "g":
            g += 1
        if char == "a":
            a += 1
        if char == "c":
            c += 1
        if char == "t":
            t += 1
print("number of g's " + str(g))
print("number of a's " + str(a))
print("number of c's " + str(c))
print("number of t's " + str(t))

# convert to floating point (0.)

gc = (g + c + 0.) / (a+t+g+c+0.)

print("gc content: " + str(gc))
