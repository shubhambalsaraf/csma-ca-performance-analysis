import numpy
import random
import matplotlib.pyplot as plt

##Assuming perfect broadcast channel - which means transmission is done instantaneoulsy.
##Assuming no collision - meaning perfect collision avoidance



nof = input('Enter the number of persistent connections:' )
print(nof)
noa = nof
X = numpy.array([])
Y = numpy.array([])

##Function keeps the count of packets
def packetswaiting(lambd):
    count = 0
    t = 0
    under1 = 1.0
    while t < under1:
        t += random.expovariate(lambd)
        count += 1
    return count

##Function to return throughput
def tput(lambd):
    buffer = 1000
    totalp = 0
    sentp = 0
    for i in range(buffer):
        totalp += (packetswaiting(lambd)*noa)
        if totalp != 0:
            sentp += 1
        else:
            sentp += 0
    return float(((sentp) / totalp))


for lambd in numpy.arange(0.01, 5, .05):
    finalt = lambd * tput(lambd)
    X = numpy.append(X, finalt)
    Y = numpy.append(Y, lambd)

plt.plot(Y, X)
plt.ylabel("Throughput\n")
plt.xlabel("Lambda\n")
plt.title("CSMA-CA %g -Persistent Connections\n" %(noa))
plt.show()