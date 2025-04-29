#Sets
#
# add()
# discard()
# clear()
# copy()
# len(set)
#
# Vergleiche mit < > <= >=  == !=
#
# frozenset(set)

einSet = set([1,2,3])

#Versuch: ein Element doppelt einfügen

einSet.add(2)

print("einSet:", einSet)

#Fazit: doppelte Einträge führen nicht zu Errors, sie werden ignoriert
#ein Set heißt in anderen Sprachen z.B. Hash

#auf Teilmengen prüfen

#einanderesSet = set([2])
einanderesSet = set([7])


if einanderesSet < einSet:
    print("Teilmenge")
else:
    print("keine Teilmenge")


namenSet = set(["Andreas", "Bettina", "Christina", "Dieter"])
namenSet.add("Erik")

print(namenSet)
#Sets sind unsortiert.

#Sortiert als Liste:
print( sorted(namenSet) )

unveraenderlichesSet = frozenset(namenSet)
#unveraenderlichesSet.add("Franz")  gibts nicht!
#unveraenderlichesSet.discard("Andreas") gibts ebenfalls nicht


