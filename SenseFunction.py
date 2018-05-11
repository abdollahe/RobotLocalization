
P = [0.2, 0.2, 0.2, 0.2, 0.2]
World = ["green" ,"red" ,"red", "green", "green"]
Z = "red"

pHit = 0.6
pMiss = 0.4


def sense(p , z):

   q =[]
   for i in range(len(p)):
       hit = (z == World[i])
       q.append(p[i] * ((hit * pHit) + ((1 - hit) * pMiss)))

   sumq = sum(q)

   for i in range(len(q)):
        q[i] = q[i] / sumq

   return q


print(sense(P, Z))

