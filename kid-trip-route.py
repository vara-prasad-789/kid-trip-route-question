a = input().split(",")
start_city = input()
b = []
for i in a:
    b += [i.split("-")]

c = []
d = []
present_city = start_city
for i in range(len(b)):
    for j in b:
        if((j[0] == present_city) and (j[0] not in d)):
            present_city = j[1]
            d += [j[0]]
            c += [("-").join(j)]
            break
for i in c:
    print(i)


# input 1 :Paris-Skopje,Zurich-Amsterdam,Prague-Zurich,Barcelona-Berlin,Kiev-Prague,Skopje-Paris,Amsterdam-Barcelona,Berlin-Kiev,Berlin-Amsterdam.
# input 2 :Kiev