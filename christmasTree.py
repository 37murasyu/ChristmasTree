# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 00:44:49 2021

@author: villa

メモ
正弦波もどきを位相をずらして４つのF
F’をそれぞれ位相ズレ版を作る
上記を実現するには、、、、？

クラスをつかうと？

iの偶奇あるいはソレ以外のなにかでイルミネーションの色を変えるには、、？
2次元配列を利用
"""

import matplotlib.animation as anm
import matplotlib.pyplot as plt
import numpy as np
import math
import random
from matplotlib.offsetbox import OffsetImage, AnnotationBbox 

import winsound
import time
 
# 実行時間計測開始
start_time = time.perf_counter()
 

class Christmas:
    def __init__(self,A,ISOU):
        self.A=A 
        self.ISOU=ISOU#位相ずれ作る
        #self.color=color
    def Function(self,i,x):#正弦波もどきを作る関数
        y=self.A*np.sin((x -ik*i)*2+self.ISOU*math.pi)*x*k
        return y
    def Derivative_function(self,i,x):#上記の関数の一階微分
        y=self.A*(2*np.cos((x-ik*i)*2+self.ISOU*math.pi)*x*k+np.sin((x -ik*i)*2+self.ISOU*math.pi)*k)
        return y

def DIV(i,k):
    #どれくらい周期でチカチカさせるか、(透明度0か正の値)、あるいは色を変えるcolor_LISTの0番か1番を選択
    if(i%k<k/2):return 0
    else:return 1
    
def imscatter(x, y, image, ax=None, zoom=1,alpha=1,): #fffff
    if ax is None: 
        ax = plt.gca() 
    try: 
        image = plt.imread(image) 
    except:
        pass 
    im = OffsetImage(image, zoom=zoom,alpha=alpha) 
    artists = [] 
    for x0, y0 in zip(x, y): 
        ab = AnnotationBbox(im, (x0, y0), xycoords='data', frameon=False) 
        artists.append(ax.add_artist(ab)) 
    return artists 
class SNOW:      
    def __init__(self,x_0,y_0,v_0,i_0):
        self.x_0=x_0 
        self.y_0=y_0
        self.v_0=v_0
        self.i_0=i_0
    def Function(self,i):#正弦波もどきを作る関数
        if(i>self.i_0):
            y=self.v_0*(i-self.i_0)+self.y_0
            x= 0.01*random.gauss(0,1)+self.x_0
        else:x=y=4
        return [x,y]
def sigmoid(x, a):
    return 1 / (1 + np.exp(-a * x))

fig = plt.figure(figsize = (10, 6))
x = np.arange(0, 10, 0.1)
x2 = np.arange(0, 9.6, 0.1)
x3=np.arange(-3, 3, 0.1)

k=0.09
a=4
b=6
ik=0.035
D_size=5#Decoration
A=2
cm = plt.get_cmap("Reds")
xl=list(range(0,360,30))
yl=[np.sin(xl) for i in xl]

interval_1=100


YLIST=[
       Christmas(A, 0/4),
       Christmas(A,2/4),
       Christmas(A, 4/4),
       Christmas(A,6/4),
       Christmas(A,1/4),
       Christmas(A, 3/4),
       Christmas(A, 5/4),
       Christmas(A,7/4)
       ]#位相いがい全て同じ関数、一階微分をクラスをもちいて作成、なぜかAは入れないとアニメーションでエラーを起こす

C_LIST=[["r","y"],
        ["r","c"],
        ["goldenrod","c"],
        ["m","w"],
        ["r","y"],
        ["r","c"],
        ["goldenrod","c"],
        ["m","w"],
        #上記は関数のカラーリスト,2次元配列にしているのはDIVを用いて一定の周期で色を変えるため。
        ["#ffd700","w"]]#トップのお星様用

SNOW_LIST=list()
for i2 in range(50):
    SNOW_LIST.append(SNOW(random.uniform(-3,3),random.uniform(-2,0), -0.2,random.randint(0,25)))
    #print(SNOW_LIST[i2].Function(0))





#y4dx=y111_DT(x, i, A, 1.5)

y5 = A *x2*k#使ってない
#y6 = Christmas(A,1.5)
#print(yl[i])


#print(y111(a, 0, k))
image_path = 'POPUKOface.png' 
image_path2 = 'lena.jpg' 

def update(i, fig_title,A):#ここもAを抜かすと何故かエラー
    #if i != 0:
    plt.cla()                      # 現在描写されているグラフを消去,
    #何故か塗りつぶしのみ0枚目も消去しないと、0枚目の透明度が機能しない
    plt.xlim(-3, 3)#xlimは横軸の範囲制限のこと,このxと１９行目２０行目のxは違う！！！
    plt.ylim(-10.1, 1.5)
                
    if i>10:
        plt.plot(YLIST[1].Function(i,a), -a, marker='o',markersize=10,color=cm(0.5))
        
    else:
        plt.plot(YLIST[1].Function(i, a), -a, marker='o',markersize=10,color=cm(0.99))
    #一個だけあるボールのコード、for文で増やす予定
    
    plt.fill_between(x3, 1,-10,facecolor="k")#背景全部黒
    #plt.fill_between(-y5, -x2-0.4,-10,facecolor="g",alpha=0.3)
    #plt.fill_between(y5, -x2-0.4,-10,facecolor="g",alpha=0.3)
    #クリスマスツリーの木の緑部分(使わないかも)
    imscatter([0], [-6], image_path2, ax=None,  zoom=.25,alpha=0.8*sigmoid(i-15, 0.4))
    
    for j in range(100):
        for j2 in range(8):
            
            if (YLIST[j2].Derivative_function(i, x[j]))<0:#(微分項がマイナスなら実行、透明度を0.5に設定薄く表示、透明度はalphaです)
                plt.plot(YLIST[j2].Function(i, x[j]), -x[j], C_LIST[j2][DIV(i, 10)]\
                         ,linestyle="dashed",marker='*',alpha=0.5)
            else:#*DIV(i+j+4*YLIST[j2].ISOU, 4)
                plt.plot(YLIST[j2].Function(i, x[j]), -x[j], C_LIST[j2][DIV(i, 10)]\
                         ,linestyle="dashed",marker='*',markersize=8,alpha=1)
    
    #for j in range(10):
        #plt.plot(0.1*random.randrange(-30,30),0.1*random.randrange(-100,0   ),marker='.',markersize=1,color="w")
    #plt.plot(0,0,marker='*',markersize=50,color=C_LIST[8][DIV(i, 10)])#トップのお星様
    #imscatter([0], [-1+1*math.cos(i*2*math.pi/0.508*interval_1)], image_path, ax=None,  zoom=.125*(1.5+math.sin(i*math.pi/10)),alpha=math.sin(i/30))
    #118Bpm=0.508s
    #plt.text(0.2, -4, "    机上の空論\n求めよさらば与えられん", color="w",size=30,fontname="MS Gothic")
    for i2 in range(50):    
        plt.plot(SNOW_LIST[i2].Function(i)[0],SNOW_LIST[i2].Function(i)[1],marker='.',markersize=5,color="w")
    plt.title(fig_title + 'k='+str(k)+',a='+str(a)+',ik='+str(ik)+',i=' + str(i))#グラフタイトル、使ってない、無視して良い
    

ani = anm.FuncAnimation(fig, update, fargs = ('Initial Animation!GREENα=0 ',2), \
                        interval = interval_1, frames = 30)#２の値はAのこと

ani.save("Christmas.gif", writer = 'imagemagick')
# 修了
end_time = time.perf_counter()
 
# 経過時間を出力(秒)
elapsed_time = end_time - start_time
print(elapsed_time)
tt=300
winsound.Beep(262,tt)  #ド（262Hzの音を1000msec流す）
winsound.Beep(294,tt)  #レ（294Hzの音を1000msec流す）
winsound.Beep(330,tt)  #ミ（330Hzの音を1000msec流す）
winsound.Beep(349,tt)  #ファ（349Hzの音を1000msec流す）
winsound.Beep(392,tt)  #ソ（392Hzの音を1000msec流す）
winsound.Beep(440,tt)  #ラ（440Hzの音を1000msec流す）
winsound.Beep(494,tt)  #シ（494Hzの音を1000msec流す）
winsound.Beep(523,tt)  #ド（523Hzの音を1000msec流す）