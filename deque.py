import collections
d = collections.deque([8, 18, 28])

print("Erstellt:", d)
print("Kopie:", d.copy())


print("Elemente:")
for x in d:
    print(x)
for i in range(len(d)):
    print(f"{i}: {d[i]}")
    
print("Deque verdoppelt:", d * 2)
print("Andere deque addiert:", d + collections.deque([9, 19, 29]))

d.clear()

print("Nach Leerung:", d)
