#Lavanya Verma
#2018155
#Section : A , Group : 3
#HW4
import math
import copy
import matplotlib.pyplot as plt
n=input('shape:')
def gen(x,y,jump):#function for generating theta (ellipse locus)
	while x<y:
		yield x
		x+=jump

def rotate(x,y,theta):# function for rotation about the origin
		theta=math.radians(theta)
		x1=copy.deepcopy(x)
		for i in range(len(x)):
			x[i]=float(x[i]*math.cos(theta)-y[i]*math.sin(theta))
			y[i]=float(x1[i]*math.sin(theta)+y[i]*math.cos(theta))
		return (x,y)
c=0
if n=="Polygon":# code segment for plotting polygon
	x=list(map(float,input("X-coordiantes: ").split(' ')))#list of x coordinates
	y=list(map(float,input('Y-coordinates: ').split(' ')))#list of y coordinates
	x=x+[x[0]]
	y=y+[y[0]]
	plt.ion()
	plt.xlabel("X-Axis")
	plt.ylabel("Y-Axis")
	while n!='quit':
		c+=1
		if n[0]=='R':
			x,y=rotate(x,y,float(n[2:]))# call rotate function saves point
		elif n[0]=='T':
			n=n.split(' ')
			x=list(map(lambda b:b + float(n[1]),x)) # Translates coordinates
			y=list(map(lambda c:c + float(n[2]),y))
		elif n[0]=="S": # Scales coordinates
			n=n.split(' ')
			x=list(map(lambda b: b*float(n[1]),x))
			y=list(map(lambda c: c*float(n[2]),y))
		print('X-coordiantes:'+' '.join(list(map(str,x))[:-1]))# printing of coordinates
		print('Y-coordinates:'+' '.join(list(map(str,y))[:-1]))
		plt.plot(x,y,label='Polgon Plot '+str(c)) #Plot vertices and edges
		plt.legend()
		plt.autoscale()
		plt.title('IP HW 4')
		n=input()
elif n=="disc":
	z,y,x=list(map(float,input().split(' '))),[],[]
	if len(z)==3:
		z.append(z[2])
	plt.ion()
	plt.xlabel("X-Axis")
	plt.ylabel("Y-Axis")
	for i in gen(0,6.28,0.01):
		x.append(z[0]+z[2]*math.cos(i))
		y.append(z[1]+z[3]*math.sin(i))
	while n!='quit':
			c+=1
			n=n.split(' ')
			if len(n)>1:
				n[1]=float(n[1])
			if len(n)>2:
				n[2]=float(n[2])
			if n[0]=="R":#rotaion
				x,y=rotate(x,y,n[1])	
			if n[0]=="T":#translation
				x=list(map(lambda k: k+n[1],x))
				y=list(map(lambda l: l+n[2],y))
			if n[0]=='S':#scaling
				x=list(map(lambda c: c*n[1],x))
				y=list(map(lambda c: c*n[2],y))
				z[2]=z[2]*n[1]
				z[3]=z[3]*n[2]
			plt.plot(x,y,label='Disc Plot '+str(c))
			plt.autoscale()
			plt.legend()
			if z[2]==z[3]:# printing of attributes according to characteristic of circle or ellipse
				print('centre: (' +str(z[0])+','+str(z[1])+') radius:'+str(z[2]))
			else:
				print('centre: (' +str(z[0])+','+str(z[1])+') axes: ('+str(z[2])+','+str(z[3])+')')
			plt.title('IP HW 4')
			n=input()
plt.close()









