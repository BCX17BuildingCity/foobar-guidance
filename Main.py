#python resources
import numpy as np
import googlemaps
from datetime import datetime
import itertools
from math import cos,pi

#classes----------------------------------------------------------------------------------------------------------

class Site(object):
    def __init__(self):
        self.location=''
        self.crowd_count=''
        self.crowd_rate=''
        self.coupons=''
        self.average_time=0

class Person(object):
    def __init__(self, Wishlist):
        self.location
        self.route=optimalRoute(Wishlist)

#declerations-----------------------------------------------------------------------------------------------------

now = datetime.now()
gmaps = googlemaps.Client(key='AIzaSyClDVamLeWK9jlFPRyTYBFnJ36lzjyp01o')
Path=[]

#functions--------------------------------------------------------------------------------------------------------

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
#math functions
def c2(x): return 0.5*cos(pi*x/12)+0.5
def c(x):
    if 7<=x and x<22:
        return 2*(x-7)/18
    if 16<=x and x<=22:
        return 3*(x-22)/18
    else:
        return 0

#def value(Master,Path):

#Sites for now hard coded------------------------------------------------------------------------------------------
Brandenburger_Tor=Site()
Reichstag=Site()
Mustafas_Gemuese_Kebab=Site()

#hardcoding addresses----------------------------------------------------------------------------------------------
Brandenburger_Tor.location='Praiser Platz, 10117 Berlin, Germany'
Mustafas_Gemuese_Kebab.location='Mehringdamm 32, 10962 Berlin, Germany'
Reichstag.location='Platz der Republik 1, 11011 Berlin, Germany'

#hardcoding c function can later be done using taylor--------------------------------------------------------------
Brandenburger_Tor.c=c2
Mustafas_Gemuese_Kebab.c=c
Reichstag.c=c

#hardcoding average time spent at each site------------------------------------------------------------------------
#time in seconds
Brandenburger_Tor.average_time=380
Mustafas_Gemuese_Kebab.average_time=380
Reichstag.average_time=380

#routine-----------------------------------------------------------------------------------------------------------
Wishlist=[Reichstag, Brandenburger_Tor, Mustafas_Gemuese_Kebab]     #List of Sites a User would like to visit

Master=list(itertools.permutations(Wishlist))                       #Master is a touple consisting of all possible permutations of the different destinations on the wishlist
for i in range(len(Master)):
    Master[i]=list(Master[i])                                       #formatting Master
    Path.append([i,pathtime(Master[i])])                            #Path should in the end contain all time steps
