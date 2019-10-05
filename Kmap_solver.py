#Lavanya Verma
#2018155
#Section A
#Group 3
"""kmap solver upto 4 variable for upgrading upto n variables, update variables list.
first input is "no. of variables"
second is minterms and dontcares given in individual parentesis seprated by d.
eg.function:(1,3,4,5)d(14,15)
"""
import copy
result=[]
variables=['w','x','y','z']
result1=[]
result2=[]
index=[]
#function generate binary values list corresponding to  minterms and dontcares 
def listgenerator(n,s):
	mint1=[]
	dont1=[]
	mint=s[s.find('(')+1:s.find(')')]
	mint=mint.split(',')
	for i in mint:
		b=bin(int(i))
		b=b[2:]
		x='0'*(n-len(b))+b	
		mint1.append(x)
	if s.count('(')==2:	#generate dontcares list if they present
		dont=s[s.rfind('(')+1:s.rfind(')')]
		dont=dont.split(',')
		for i in dont:
			c=bin(int(i))
			c=c[2:]
			x='0'*(n-len(c))+c
			dont1.append(x)
	return(mint1,dont1)
#code unit for comparing individual terms
def compare(m,n):
	c=0
	d=0
	v=''
	for i in range(len(m)):
		if m[i]==n[i]:
			v+=str(m[i])
		else:
			c+=1
			v+='-'
	if c>1:
		j=None
	else:
		j=v
	return(j)
#generate all possible dontcare combination with minterms
def dontcare(mint1,dont1): 
	for i in range(2**len(dont1)):
		x=bin(i)[2:]
		x='0'*(len(dont1)-len(x))+x
		v=[]
		minterms1=copy.deepcopy(mint1)
		for j in range(len(x)):
			c=x.find('1',j)
			if c!=-1:
				v.append(c)
		v=list(set(v))
		for i in v:
			minterms1.append(dont1[i])
		c=minimize(minterms1)
		result.append(c)
#minimize given list of binary data
def minimize(data):
	list1=list(set(data))
	c1=[]
	mark=[0]*len(list1) 
	for i in range(len(list1)):
		for j in range(i+1,len(list1)):
			c=compare(list1[i],list1[j])
			if c!=None :
				c1.append(c)
				mark[i]=1
				mark[j]=1
			else:
				continue
	for c in range(len(list1)):
		if mark[c]==0:
			c1.append(list1[c])
	c1=list(set(c1))
	if sorted(list1)==sorted(c1):
		return c1
	else:
		return minimize(c1)
#formatting in required format
def requiredformat(resdat):
	resdat=list(map(list,resdat))
	for i in range(len(resdat)):
		for j in range(len(resdat[i])):
			if resdat[i][j]=='1':
				resdat[i][j]=variables[j]
			elif resdat[i][j]=='0':
				resdat[i][j]=variables[j]+"'"
			else :
				continue
		resdat[i]=''.join(resdat[i])
	resdat='+'.join(resdat)
	resdat=resdat.replace('-','')
	resdatt=resdat.replace("'",'')
	result2.append(resdatt)
	return(resdat)

def minFunc(n,s):
	result3=[]
	l=listgenerator(n,s)#list generation for minterms and dontcares
	dontcare(mint1=l[0],dont1=l[1]) #call for generating all possible combination
	for i in result:#loop for formatting
		c=requiredformat(i)
		result1.append(c)
	xl=100
	for cn in range(len(result2)):
		if	xl>=len(str(result2[cn])):
			xl=len(str(result2[cn]))
	for m in result2: #if two minterms have same lenght
		if len(m)==xl:
			index.append(result2.index(m))
	for h in range(len(result1)):
		if h in index:
			result3.append(result1[h])
		else:
			continue
	result3=' OR '.join(result3)
	print('Simplified expression: '+str(result3)) 
	return(result3)
if __name__=='__main__':
	n=int(input('No. of variables: '))
	s=input('function: ')
	minFunc(n,s)
