#python resources
import numpy as np
import googlemaps
from datetime import datetime
import time
import itertools
from math import cos,pi
import sys
#classes----------------------------------------------------------------------------------------------------------

class Site(object):
    def __init__(self):
        self.name=''
        self.location=''
        self.crowd_count=''
        self.crowd_rate=''
        self.coupons=''
        self.average_time=0
class Person(object):
    def __init__(self):
        self.location=''
#declerations-----------------------------------------------------------------------------------------------------

now = datetime.now()
gmaps = googlemaps.Client(key='AIzaSyClDVamLeWK9jlFPRyTYBFnJ36lzjyp01o')
Path=[]

#functions--------------------------------------------------------------------------------------------------------
def Startup():
    Me=Person()
    y=(sys.argv[1:])        #UID,Geolocation
    x=[]
    for i in y:
        x.append(i.replace('-',''))
    print(x)
    Me.location=x[1]
    Wish=Loader(True,x[0])
    Me.Wishlist=[]
    for i in Wish:
        n=Loader(0,i)
        print('n: ',n)
        exec(n[0] + " =Site()")
        exec(n[0]+'.name=n[1]')
        exec(n[0]+'.location=n[2]')
        exec(n[0]+".average_time=int(n[3])")
        exec(n[0]+'.c='+n[4])
        exec('Me.Wishlist.append('+n[0]+')')
    return Me
def Loader(U,name):
    if U==True:
        print('looking for',name)
        with open('Data.txt', 'r') as inF:
            for line in inF:
                print(line)
                if name in line:
                    print('Found User')
                    return line.split(':')[2:-1]
    else:
        with open('Sites.txt', 'r') as inF:
            for line in inF:
                if name in line:
                    return str(line).split(':')



def Travel_time(From, To):
    directions_result = gmaps.directions(From, To, mode="transit", departure_time=now)
    a=directions_result[0]['legs']
    a=a[0]['duration']
    return int(a['value'])
def pathtime(path):
    time=[]
    for i in range(len(path)-1):
        time.append(Travel_time(path[i].location,path[i+1].location))
    return time
#math functions should in a actual product be created using at least taylor and machine learning
def c2(x): return 0.5*cos(pi+x/12)+0.5
def c(x):
    if 7<=x and x<16:
        return 2*(x-7)/18
    if 16<=x and x<=35/2:
        return 1
    if 25/2<x and x<22:
        return -4*(x-22)/18
    else:
        return 10000000
def c1(x):
        if 7<=x and x<16:
            return 3*(x-7)/18
        if 16<=x and x<=22:
            return 2*(x-22)/18
        if 22<x and x<=27:
            return 0.5
        else:
            return 10000000
def Time(Master,Path):
    Time=[]
    for y in range(len(Path)):
        time=[Path[y][1][0]]
        x=0
        for i in range(len(Path[y][1])-1):
            x+=1
            time.append(time[i]+Path[y][1][i]+Master[y][i+1].average_time)
        time.append(time[x]+Master[y][x].average_time)
        Time.append(time)
    return Time
def value(Master,times):
    Names=[]
    True_times=[]     #contains the time values as of hours since the beginning of the day to use in predicting functions
    for time in times:
        x=[]
        for n in time:
            a=float(n+(now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds())/3600
            if a>24:    #maximum amount of hours in a day
                a-=24
            x.append(a)
        True_times.append(x)
    Value=[]
    Maximum_times=[]
    for i in True_times:
        x=i[len(i)-1]-i[0]
        if x<0:
            x+=24
        Maximum_times.append(x)
    Value=[]
    for q in range(len(Master)):
        x=[]
        for i in range(1,len(Master[q])):
            x.append(Master[q][i].c(True_times[q][i]))
        Value.append(sum(x))
    a=100000000000000
    for q in range(len(Value)):
        Value[q]=[q,a*Value[q]+Maximum_times[q]]
    return Value

#Sites for now hard coded------------------------------------------------------------------------------------------
Me=Startup()

#routine-----------------------------------------------------------------------------------------------------------
Master=list(itertools.permutations(Me.Wishlist))                       #Master is a touple consisting of all possible permutations of the different destinations on the wishlist
for i in range(len(Master)):
    Master[i]=list(Master[i])                                       #formatting Master
    Names=[]
    print(Master)
    for n in Master[i]:
        Names.append(n.name)
    Master[i].insert(0,Me)
    Path.append([Names,pathtime(Master[i])])                            #Path should in the end contain all time steps
times=Time(Master,Path)
Value=value(Master,times)
Bestfit=0
for i in range(1,len(Value)):   #lol that time safe :o <3
    if Value[i][1]<Value[Bestfit][1]:
        Bestfit=i
print(Master[Bestfit])
for i in range(1,len(Master[Bestfit])):
    print(Master[Bestfit][i].name)
