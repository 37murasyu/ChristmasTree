# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 01:53:50 2021

@author: villa
"""


import matplotlib.animation as anm

import math
import numpy as np
import matplotlib.pyplot as plt
import winsound
from datetime import datetime,date
a=datetime.now()
b=date.today().strftime('%Y年%m月%d日')

θ1=0
#θ2=0
l1=2
l2=2

P1=P2=[0,0]
LOG=list()
LOG1=list()
kakusuu=7
countUP=0
countUP2=0
countUP4=0
NoFALSE=0
N=15

fig = plt.figure(figsize = (10, 6))
def LINK_Plot(x,y,P1,A):
    plt.plot(x, y,color=A, marker='.',markersize=13)
    plt.plot(P1[0], P1[1],color=A, marker='.',markersize=11)
    plt.plot([P1[0], x], [P1[1], y],color=A)
    plt.plot([0,P1[0]], [0,P1[1]],color=A)
    LOG.append([x,y])
    
def GYAKU_UNDOGAKU(x,y):
    C1=(x**2+y**2+l1**2-l2**2)/(2*l1)
    #C2=(x**2+y**2-l1**2+l2**2)/(2*l2)
    θ1=math.atan2(y, x)+math.atan2(math.sqrt(x**2+y**2-C1**2),C1)
    θ2=math.atan2(y-l1*math.sin(θ1), x-l1*math.cos(θ1))-θ1
    return[θ1,θ2]

def IDOU(x_0,y_0,x_End,y_End):
    [θ1,θ2]=GYAKU_UNDOGAKU(x_0, y_0)
    #θ2=GYAKU_kaiseki(x_0, y_0)[1]
    LOG1.append([θ1,θ2])   
    for iii in range(N):
        P1=[l1*(math.cos(θ1)),#
            l1*math.sin(θ1)]#
        
        P2=[l2*(math.cos(θ1+θ2)),#
            l2*math.sin(θ1+θ2)]#
        x=P2[0]+P1[0]
        y=P2[1]+P1[1]
        J=np.array([[-P1[1]-P2[1],-P2[1]],[P1[0]+P2[0],P2[0]]])
        [[dθ1],[dθ2]]=np.dot(np.linalg.inv(J),[[(x_End-x_0)/N],[(y_End-y_0)/N]])
        θ1+=dθ1
        θ2+=dθ2
        #E=np.dot(np.linalg.inv(J),J)
        #print(E)
        LOG1.append([θ1,θ2])
    return LOG1
"""
class ENKO:
    def __init__(self,a,b,r):
        self.a=a
        self.b=b
        self.r=r
    def FUNC_UP(self,x):
        y=self.b+math.sqrt(self.r**2-(x-self.a)**2)
        return y
    def FUNC_DOWN(self,x):
        y=self.b-math.sqrt(self.r**2-(x-self.a)**2)
        return y
    def BIBUN_ENKO_SHITA(self,x):
        dy=(self.a-x)/math.sqrt(self.r**2-(x-self.a)**2)
        return dy
O1=ENKO(0+1, 0.5, 0.5)"""
    
def IDOU_Curve(x_0,y_0,θ_0,θ_End,r):#(degree)
    [θ1,θ2]=GYAKU_UNDOGAKU(x_0, y_0)
    LOG1.append([θ1,θ2])
    N1=round(50*(θ_End-θ_0)/360)
    for iii in range(N1):
        Φ=(θ_End-θ_0)/180*math.pi*iii/N1+θ_0/180*math.pi
        P1=[l1*(math.cos(θ1)),#
            l1*math.sin(θ1)]#
        #2*math.pi/N1
        P2=[l2*(math.cos(θ1+θ2)),#
            l2*math.sin(θ1+θ2)]#
        x=P2[0]+P1[0]
        y=P2[1]+P1[1]
        J=np.array([[-P1[1]-P2[1],-P2[1]],[P1[0]+P2[0],P2[0]]])
        [[dθ1],[dθ2]]=np.dot(np.linalg.inv(J),[[-r*math.sin(Φ)*2*math.pi/N1],[r*math.cos(Φ)*2*math.pi/N1]])
        #-O1.r*math.sin(2*math.pi*iii/N1)*2*math.pi*iii/N1だとなぜ駄目なのかわからない
        
        θ1+=dθ1
        θ2+=dθ2
        #E=np.dot(np.linalg.inv(J),J)
        #print(E)
        LOG1.append([θ1,θ2])
Alphabet={"A":((1,0,1,-.5,0),
               (1,0,1,.5,0),
               (1,-1/3,1/3,1/3,1/3)),
          "E":((1,-.5,1,-.5,0),
               (1,-.5,1,.5,1),
               (1,-.5,.5,.25,.5),
               (1,-.5,0,.5,0)),
          "H":((1,-.3,1,-.3,0),
               (1,.3,1,.3,0),
               (1,-.3,.5,.3,.5)),
          "M":((1,-.5,1,-.5,0),
               (1,-.5,1,0,.5),
               (1,.5,1,0,.5),
               (1,.5,1,.5,0)),
          "N":((1,-.5,1,-.5,0),
               (1,-.5,1,.5,0),
               (1,.5,1,.5,0)),
          "O":((0,0,1,90,450,0.5),
               (0,0,1,90,450,0.5)),
          "U":(((1,-.5,1,-.5,.5),
                (1,.5,1,.5,.5),
                (0,-.5,.5,180,360,.25))),
          "X":((1,-.5,1,.5,0),
               (1,.5,1,-.5,0)),
          "∀":((1,0.2,0,-.5,1,1),
               (1,0.2,0,.5,1,1),
               (1,-1/3,2/3,1/3,2/3,1))}
"""
IDOU(0-1, 1, -0.5-1, 0)
IDOU(0-1, 1, .5-1, 0)
IDOU(-1/3-1, 1/3, 1/3-1, 1/3)
"""

def MOZI(*MOZI):#何文字でも受付可
    print(MOZI)
    LL=len(MOZI)
    print(MOZI[0])    
    for i in range(LL):
#       print(Alphabet[MOZI[i]][0])
        for j in range(len(Alphabet[MOZI[i]])):
            print(Alphabet[MOZI[i]][j])
            AA=Alphabet[MOZI[i]][j]
            if(AA[0]==1):
                IDOU(AA[1]-2.2+1.1*i, AA[2], AA[3]-2.2+1.1*i, AA[4])
            else:
                IDOU_Curve(AA[1]-2.2+1.1*i, AA[2], AA[3], AA[4], AA[5])


"""
mozi=a,b,c
mozi[0]=a
Alphabet[mozi[0]]=(,),(,),,,,(aについて「)
Alphabet[mozi[0]][0]=(,,,)

mozi
"""

MOZI("N","E","M","U") 
"""
IDOU(-0.3, 1, -.3, 0)
IDOU(.3, 1, .3, 0)
IDOU(-.3, .5, .3, .5)

IDOU_Curve(-.5+1+1,O1.FUNC_DOWN(-.5+1+1),40)
#IDOU_Curve(-.5+1+0.1, .5+1-.1, O1.FUNC_UP(-.5+1+.1),1)
for i in range(3):
    LOG1.append(GYAKU_UNDOGAKU(0.2, 0.2))"""

"""
P1=[l1*(math.cos(θ1)),#
    l1*math.sin(θ1)]#

P2=[l2*(math.cos(θ1+θ2)),#
    l2*math.sin(θ1+θ2)]#
x=P2[0]+P1[0]
y=P2[1]+P1[1]
LINK_Plot(x, y, P1, "k")
""""""
for i in range(50):
    
    P1=[l1*(math.cos(θ1)),#
        l1*math.sin(θ1)]#
    
    P2=[l2*(math.cos(θ1+θ2)),#
        l2*math.sin(θ1+θ2)]#
    x=P2[0]+P1[0]
    y=P2[1]+P1[1]
    J=np.array([[-P1[1]-P2[1],-P2[1]],[P1[0]+P2[0],P2[0]]])
    [[dθ1],[dθ2]]=np.dot(np.linalg.inv(J),[[0],[-.1]])
    θ1=dθ1+θ1
    θ2=dθ2+θ2
    LOG1.append([θ1,θ2])
#GYAKU_kaiseki(2, 1)"""
print(len(LOG1))

def update(i, fig_title,A):

    #if i != 0:
    plt.cla()   
                       # 現在描写されているグラフを消去,
    #何故か塗りつぶしのみ0枚目も消去しないと、0枚目の透明度が機能しない
    plt.xlim(-3, 3)#xlimは横軸の範囲制限のこと,このxと１９行目２０行目のxは違う！！！
    plt.ylim(-1, 3)
    for j in range(len(LOG)):
        plt.plot(LOG[j][0], LOG[j][1],"g",marker='.')
        
#for II in range(2):
    
#for i in range(0,180,2):
    print("i is No",i)

    θ1=LOG1[i][0]
    θ2=LOG1[i][1]
    P1=[l1*(math.cos(θ1)),#
        l1*math.sin(θ1)]#
    
    P2=[l2*(math.cos(θ1+θ2)),#
        l2*math.sin(θ1+θ2)]#
    x=P2[0]+P1[0]
    y=P2[1]+P1[1]
    #plt.plot(x, y,color="k", marker='.',markersize=11)
    LINK_Plot(x, y, P1, "k")
        
    
#plt.plot(P1[0],P1[1],marker='*',markersize=15)
    #plt.title(fig_title + 'i=' + str(5*(i))+',1=' +str(countUP)+',2=' +str(countUP2)+',4=' +str(countUP4))
    

ani = anm.FuncAnimation(fig, update, fargs = ('Initial Animation!GREENα=0 ',1), \
                       interval = 50, frames = len(LOG1))

ani.save("SERIAL_LINK1.gif", writer = 'imagemagick')
plt.show()
LOG1.clear()
winsound.Beep(500, 1000)
