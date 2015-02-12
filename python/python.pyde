import types 
table=loadTable("/Users/Kevin/desktop/CS582/02Tree/tree.csv");#READ THE DATA FROM FILE just select 20 tuples
multilist = [[0 for col in range(18)] for row in range(20)]# create a list to store the value in the matrix
alist = [[0 for col in range(3)] for row in range(19)]# create a list to store the position
t=20 #local variable

for j in range(18):#initialize
    for i in range(20):
        multilist[i][j]=(table.getString(i,j))
        #multilist[i][0]=i

def setup():
    size(900, 1000)#the size
    frameRate(1)
    for i in range(20):
        multilist[i][0]=i # change the name to help remember
    line(20,0,20,440)# the y axle
    line(20,440,900,440)# the x axle
    for i in range(19):
        text(i+1,20,410-i*20)# to mark the degree
    for i in range(20):
        text(i,40*(i+1),440) # to mark the position
    
    
def draw():
    fill(255)
    tree() # plot the tree
    if(t<2):
        lines() # connect the node
        

def distance(a=[],b=[]):# calculate the distance by euclidean distance
    distance = 0.0
    for i in range(1,18):
        distance += (float(a[i])-float(b[i]))*(float(a[i])-float(b[i]))
    return distance
                            
def position(a=[],b=[]): # to calcuate the middle position after clustering
    p=[(a[0]+b[0])/2.0,]
    for i in range(len(a)-1):
        p.append((float(a[i+1])+float(b[i+1]))/2)
    return p

def tree():# plot the tree
    global t
    mark1=-1 # the position 1 need to be clustered
    mark2=-1 # the position 2 need to be clustered
    mark3=-1 # the middle position after clustering
    D=[]
    i=0
    
    if len(multilist)>=2: # when the cluster will stop ~ smaller than 2 node
        
        while i < len(multilist)-1: #put all the distance in the multilist
            j = i+1
            while j < len(multilist):
                D.append(distance(multilist[i],multilist[j]))
                j= j+1
            i=i+1

    
        k=0
        while k< len(multilist)-1:#calculate the samllest distance and the position
            l = k +1
            while l< len(multilist):
                if distance(multilist[k],multilist[l])==min(D):
                    mark1 = multilist.pop(k)
                    mark2 = multilist.pop(l-1)
                    mark3 = (position(mark1,mark2))
                    multilist.append(mark3)
                    alist[20-t][0]=mark1[0]
                    alist[20-t][1]=mark2[0]
                    l=20
                    k=19
                l = l+1
            k=k+1
        #print "level" ,mark1[0],mark2[0],mark3[0]
        #print "\n"
        alist[20-t][2]=t; # mark the height of clustering
        if(type(mark1[0])==type(1)):
             fill(255,0,0)# when the node is the data,mark red
             text(mark1[0],40*(mark1[0]+1),20*t)# mark the position
        rect(40*(mark1[0]+1),20*t,20,10)
        fill(255)
        if(type(mark2[0])==type(1)):
            fill(255,0,0)# the node is the data,mark red
            text(mark2[0],40*(mark2[0]+1),20*t)#mark the position
        rect(40*(mark2[0]+1),20*t,20,10)
   
        t-=1
            
def lines():# connect all the nodes.
    for i in range(19):
        for j in range(19):
            if i!=j:
                if(type(alist[i][0])==type(1.0)):
                    if alist[i][0] == (alist[j][0]+alist[j][1])/2.0:
                        line(40*(alist[i][0]+1),20*alist[i][2],40*(alist[j][0]+1),20*alist[j][2])
                        line(40*(alist[i][0]+1),20*alist[i][2],40*(alist[j][1]+1),20*alist[j][2])
                if(type(alist[i][1])==type(1.0)):
                    if alist[i][1] == (alist[j][0]+alist[j][1])/2.0:
                        line(40*(alist[i][1]+1),20*alist[i][2],40*(alist[j][0]+1),20*alist[j][2])
                        line(40*(alist[i][1]+1),20*alist[i][2],40*(alist[j][1]+1),20*alist[j][2])                   
           

        
   
    
           



