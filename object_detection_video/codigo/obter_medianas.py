import cv2
import numpy as np
import pickle
import numbers
d =pickle.load(open('outro.p','rb'))
print(d.keys())
p=d["outro"]

p.sort()

x=len(p)/2

a=0
if(isinstance(x,int)):
	a=(p[x]+p[x+1])/2
else:

	a=p[int(x)]
print(a)

#print(len(p))