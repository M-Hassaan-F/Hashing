studArr = []
for x in range(10):
    print("Enter record key:")
    RK = input()
    InsertHash(RK)

print("Enter search record key:")
RK = input()
x = SearchHash(RK)
if x == 0:
    print("Not found")
else:
    print("found")

for x in range(10):
    print(studArr(x))


def InsertHash(RecKey):
    HashKey = Hash(RecKey, 10)
    while  studArr(HashKey) != 0:
        HashKey = HashKey + 1
        if HashKey > 10:
            Hashkey = 0
    studArr.insert(HashKey, RecKey)


def SearchHash(RecKey):
    hashkey = Hash(RecKey, 10)
    while studArr(hashkey) != Reckey:
        totsearches = totsearches + 1
        hashkey = hashkey + 1
        if hashkey > 10:
            hashkey = 0
            if totsearches > 10:
                return 0
    return hashkey



def Hash(KeyVal, MaxPos):
    indexpos = KeyVal%MaxPos+1
    return indexpos



