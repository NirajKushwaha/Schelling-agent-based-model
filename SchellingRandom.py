import numpy as np 
import random as r 
import matplotlib.pyplot as plt 

nodes = int(input("Enter the total number of nodes in the network(Sample Input- 100): "))
probability = float(input("Enter the probability of connection in the required random network(Sample Input- 0.1): "))



#<===========Start: Creating a undirected random network using ER Algorithm===========>
adjMatrix = np.zeros((nodes , nodes))

for i in range(nodes):
    for j in range(nodes):
        if(i > j):
            randomNum = r.uniform(0 , 1)
            if(randomNum <= probability):
                adjMatrix[i][j] = 1
                adjMatrix[j][i] = 1
#<===========End: Creating a undirected random network using ER Algorithm===========>



xPercent = float(input("Enter the percent of x agents in the system(Sample Input- 50): "))
ratio = xPercent/100

tolerance = float(input("Enter the similarity threshold of the agents in percent(Sample Input- 80): "))


#<===========Start: Categorizing the nodes in two types of agents===========>
nodeList = [x for x in range(nodes)]
xNodes = r.sample(nodeList , int(ratio*nodes))
yNodes = [x for x in nodeList if x not in xNodes]

nodeCategoryList = []
for i in range(nodes):
    if(i in xNodes):
        nodeCategoryList.append(-1)     #-1 represents agent of type x
    else:
        nodeCategoryList.append(1)      #1 represents agent of type y
#<===========End: Categorizing the nodes in two types of agents===========>



#<===========Start: Function to identify if a node is satisfied with it's curretn connections or not===========>
def satisfactionCalculation(u , same , different):
    for v in range(nodes):
        if(adjMatrix[u][v] == 1):
            if(nodeCategoryList[u] == nodeCategoryList[v]):
                same += 1
            else:
                different += 1
        else:
            pass
    
    if(same+different == 0):
        return 100
    else:
        return ((same/(same+different))*100)
#<===========End: Function to identify if a node is satisfied with it's curretn connections or not===========>



#<===========Start: Function to calculate percentage of nodes which are satisfied===========>
def happyCalculator():
    happy = 0
    for z in range(nodes):
        satisfy = satisfactionCalculation(z , 0 , 0)

        if(satisfy >= tolerance):
            happy += 1
        else:
            pass

    return ((happy/nodes)*100)
#<===========End: Function to calculate percentage of nodes which are satisfied===========>


step = 0
parameter = 0
parameterList = []
cyc = 0
cycle = []
while(step != 20 and parameter != 100):
    for i in range(nodes):
        satisfaction = satisfactionCalculation(i , 0 , 0)

        if(satisfaction >= tolerance):
            pass
        else:
            for j in range(nodes):
                if(adjMatrix[i][j] == 1):
                    if(nodeCategoryList[i] == -nodeCategoryList[j]):
                        a = 0
                        while(a == 0):
                            randTemp = r.randint(0 , nodes-1)
                            if(randTemp != i and adjMatrix[i][randTemp] == 0):
                                adjMatrix[i][randTemp] = 1
                                adjMatrix[i][j] = 0
                                a += 1

                                parameter = happyCalculator()
                                parameterList.append(parameter)
                                #print(parameter)

                                cyc += 1
                                cycle.append(cyc)
                            else:
                                pass
                            
                if(satisfactionCalculation(i , 0 , 0) >= tolerance):
                    break
                else:
                    pass

    step += 1

font = {'family': 'serif',
        'color':  'black',
        'weight': 'bold',
        'size': 17,
        }

plt.xlabel("Number of steps" , fontdict = font)
plt.ylabel("% of nodes satisfied" , fontdict = font)


plt.plot(cycle , parameterList)
plt.show()



            