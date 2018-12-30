import math

#v=[[150,170,100],[5,10,60],[70,100,200],[200,215,240],[10,15,70],[180,175,160],[75,95,100],[140,100,110],[5,10,15],[15,20,45],[60,65,170],[150,160,180],[25,50,75],[170,180,190],[10,15,50],[80,90,100]]
v=[]
n=int(input("enter the number of elements"))

for i in range(n):
    v.append(list(map(int,input().rstrip().split())))
from PIL import Image

import numpy as np

img=Image.open('color.jpg','r')

v=list(img.getdata())


a1=v[0][0]
a2=v[0][1]
a3=v[0][2]

b1=v[1][0]
b2=v[1][1]
b3=v[1][2]

c1=v[2][0]
c2=v[2][1]
c3=v[2][2]

a=[v[0]]
b=[v[1]]
c=[v[2]]


for i in range(3,len(v)):
    if(math.sqrt(math.pow((v[i][0]-a1),2)+math.pow((v[i][1]-a2),2)+math.pow((v[i][2]-a3),2)) < math.sqrt(math.pow((v[i][0]-b1),2)+math.pow((v[i][1]-b2),2)+math.pow((v[i][2]-b3),2))  and math.sqrt(math.pow((v[i][0]-a1),2)+math.pow((v[i][1]-a2),2)+math.pow((v[i][2]-a3),2)) < math.sqrt(math.pow((v[i][0]-c1),2)+math.pow((v[i][1]-c2),2)+math.pow((v[i][2]-c3),2))):
        a.append(v[i][0])
        a1=(v[i][0]+a1)/2
        a2=(v[i][1]+a2)/2
        a3=(v[i][2]+a3)/2
    elif(math.sqrt(math.pow((v[i][0]-b1),2)+math.pow((v[i][1]-b2),2)+math.pow((v[i][2]-b3),2)) < math.sqrt(math.pow((v[i][0]-a1),2)+math.pow((v[i][1]-a2),2)+math.pow((v[i][2]-a3),2))  and math.sqrt(math.pow((v[i][0]-b1),2)+math.pow((v[i][1]-b2),2)+math.pow((v[i][2]-b3),2)) < math.sqrt(math.pow((v[i][0]-c1),2)+math.pow((v[i][1]-c2),2)+math.pow((v[i][2]-c3),2))):
        b.append(v[i])
        b1=(v[i][0]+b1)/2
        b2=(v[i][1]+b2)/2
        b3=(v[i][2]+b3)/2
    elif(math.sqrt(math.pow((v[i][0]-c1),2)+math.pow((v[i][1]-c2),2)+math.pow((v[i][2]-c3),2)) < math.sqrt(math.pow((v[i][0]-a1),2)+math.pow((v[i][1]-a2),2)+math.pow((v[i][2]-a3),2))  and math.sqrt(math.pow((v[i][0]-c1),2)+math.pow((v[i][1]-c2),2)+math.pow((v[i][2]-c3),2)) < math.sqrt(math.pow((v[i][0]-b1),2)+math.pow((v[i][1]-b2),2)+math.pow((v[i][2]-b3),2))):
        c.append(v[i])
        c1=(v[i][0]+c1)/2
        c2=(v[i][1]+c2)/2
        c3=(v[i][2]+c3)/2


d=b+c
e=d+a





sube=[e[i:i+64]for i in range(0,len(e),64)]
arr=np.array(sube,dtype=np.uint8)


new_image=Image.fromarray(arr)

new_image.save('finaloutput1.png')



