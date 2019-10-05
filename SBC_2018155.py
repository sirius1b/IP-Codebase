#Lavanya Verma
#2018155
#Section A group 3
#hw3 of IP 
import ast
from copy import deepcopy
vertices=input('Enter vertices:')
edges=input('Enter edges:')
vertices=ast.literal_eval(vertices)
edges=ast.literal_eval(edges)
edges = list(map(lambda x: x[::-1],edges))+ edges
#function for calculating all paths from starting node to ending node (DFS implemented)
paths=[]
visited=[]
def allpath(a,l,path=[]):
	path.append(a)
	visited.append(a)
	if a==l:
		c=deepcopy(path)
		paths.append(c)
	else:
		for i in edges:
			if i[0]==a and i[1] not in visited:
				allpath(i[1],l,path)
	path.remove(a)
	visited.remove(a)
#Function returns no. of nodes in shortest path from source node to destination node including source and destination(BFS implemented)
que=[]
visitbfs={}
def shortestpath(a,l):
	global que
	que.append(a)
	c=0
	while len(que)!=0:
		c+=1
		if c>1:
			for k in visitbfs:
				if k==que[0]:
					c=visitbfs[k]+1
		if que[0]==l:
			que.clear()
			visitbfs.clear()
			return c
		else:
			for i in edges:
				if i[0]==que[0] and i[1] not in visitbfs and i[1] not in que:
					que.append(i[1])
					visitbfs[i[1]]=c
		que=que[1:]

shortpath=[]
dshort=[]#shortest path contain v
btcen={ k:v for (k,v) in zip(vertices,[0]*len(vertices))}#beteween centrality of each element
#algorithm calculate between centrality of each node.
for v in vertices:
	covered=[]
	for v1 in vertices:
		for v2 in vertices:
			if (not any([v1==v2,v2==v,v==v1])) and sorted([v1,v2]) not in covered:
				allpath(v1,v2)
				covered.append(sorted([v1,v2]))
				for i in paths:
					if len(i)<=shortestpath(v1,v2):
						shortpath.append(i)
				for j in shortpath:
					if v in j:
						dshort.append(j)
				if len(shortpath)!=0:
					btcen[v]+=int(len(dshort))/int(len(shortpath))
				else:
					continue
				dshort.clear()
				shortpath.clear()
				paths.clear()
m=max(btcen.values())
fo={}
for i in btcen:
	if btcen[i]==m:
		fo[i]=m
#decorated print
print('=='*31)
print("Top nodes with equal standardized betweenness centrality score:" )
for i in fo:
	print("Score of node "+str(i)+' is '+str((fo[i]*2)/(len(vertices)-1)*(len(vertices)-2)))
print('=='*31)













