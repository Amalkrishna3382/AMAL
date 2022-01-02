inp = input().strip()
inp = inp.split()
for i in range(len(inp)):
    inp[i] = int(inp[i])


class UnionFind:
    def _init_(self, inp):
        self.x = inp[1:]
        self.x = range(max(self.x)+1)
        self.x = list(self.x)

    def size(self, k):
        s = 0
        for i in self.x:
            a = self.find(i)
            b = self.find(k)
            s += int(a == b)
        return s

    def union(self, a, b):
        x= self.find(a)
        y=self.find(b)
        if self.size(x) > self.size(y):
            temp = a
            a = b
            b = temp
        elif self.size(x) == self.size(y):
            if x > y:
                temp = a
                a = b
                b = temp
        self.x[self.find(a)] = self.find(b)

    def find(self, y):
        while(y != self.x[y]):
            y = self.x[y]
        return y



line = input()
x = UnionFind(inp)
line=line.split()[1:]
for i in range(len(line)):
    line[i] = int(line[i])
y = input().strip().split()
[x.union(line[i], line[i+1]) for i in range(0, len(line)-1, 2)]
if y[0] == "N":
    z=0
    for i in inp[1:]:
        if x.x[i]==i:
            z+=1
    print(z)
elif(y[0] == "F"):
    k=[]
    for i in y[2:]:
        k.append(int(i))
    for i in k:
        z = x.find(i)
        print(z, end=" ")
elif(y[0] == "Z"):
    k = []
    for i in y[2:]:
        k.append(int(i))
    for i in k:
        z = x.size(x.find(i))
        print(z, end=" ")
elif(y[0] == "S"):
    k = []
    for i in y[2:]:
        k.append(int(i))
    for i in k:
        z=0
        if x.x[i] == i:
            print(z, end=" ")
        else:
            for j in inp[1:]:
                if x.x[j] == x.x[i] and j != i and j != x.x[i]:
                    z+=1
            print(z, end=" ")
elif(y[0] == "D"):
    k = []
    for i in y[2:]:
        k.append(int(i))
    for i in k:
        z = 0
        temp = i
        while x.x[temp] != temp:
            temp = x.x[temp]
            z += 1
        print(z, end=" ")