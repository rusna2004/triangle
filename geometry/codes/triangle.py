import numpy as np
import math
I=(1/(math.sqrt(37) + 4 + math.sqrt(61)))*np.matrix([[math.sqrt(61) - 16 - 3*math.sqrt(37)],[-math.sqrt(61) + 24 - 5*math.sqrt(37)]]) #Here I is incentre (point of intersection of angle bisectors)
n = np.matrix([11, 1]) #n is normal vector 
r = abs(np.dot(n,I) + 38)/(np.linalg.norm(n)) #r is distance between I and BC (nI+38=0, n and I are vectors)
print(r)
