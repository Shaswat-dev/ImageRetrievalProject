from PIL import Image
import webbrowser
import sys
import random
import math
import time
import numpy
#import histodict

class MyImage:
    def __init__(self,fname,method):
    
     self.im = Image.open(fname)
             
     self.size = self.im.size
     self.pixels = self.size[0] * self.size[1]
     self.data = list(self.im.getdata())
     self.h = self.im.histogram()
     inf = open('histodict.txt','r')
     self.histograms = eval(inf.read())
     inf.close()
     print ('Dictionary of Histograms imported')
     if method == 1:
        self.distances()
     if method == 2:
        self.intersection()
        
    def compare(self,mainimage,secondimage):
        total = 0
        hist2 = self.histograms[secondimage]
        for i in range(len(hist2)):
            a = (hist2[i]-self.h[i])**2
            total += a
        return math.sqrt(total)
        
    def distances(self):
        self.distancewith = []
        for i in self.histograms:
         a = self.compare(self.im,i)
         a = math.floor(a)
         self.distancewith.append([int(a),i])
        self.radixsort(self.distancewith)
        
    def compareintersect(self,secondimage):
        total = 0
        hist2 = self.histograms[secondimage]
        for i in range(len(hist2)):
            if hist2[i]<self.h[i]:
                total +=hist2[i]
            else:
                total +=self.h[i]
        return (float(total)/float(self.pixels))
        
    def intersection(self):
        self.intersections = []
        for i in self.histograms:
          a = self.compareintersect(i)
          a *=1000
          a = math.floor(a)
          self.intersections.append([int(a),i])
        self.radixsort(self.intersections)
        self.intersections.reverse()
    
    def radixsort(self,aList):
       RADIX = 10
       maxLength = False
       tmp , placement = -1, 1
    
       while not maxLength:
          maxLength = True
          buckets = [list() for _ in range(RADIX)]
        
          for i in aList:
            tmp = i[0] / placement
            buckets[int(tmp % RADIX)].append(i)
            if maxLength and tmp > 0:
                maxLength = False
                
          a = 0
          for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                aList[a] = i
                a += 1
                
          placement *= RADIX