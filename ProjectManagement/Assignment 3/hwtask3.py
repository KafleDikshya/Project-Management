import numpy as np
import math

number = 10000
num = 32
duration = np.array([0,9,5,9,10,8,1,10,6,3,9,10,4,2,4,10,9,9,10,1,7,9,5,5,3,8,4,2,1,7,8,0], dtype=np.int32)
opduration = duration*0.8   #Activity duration follows beta(a, b, 3- , 3+ ), a=0.8*duration, b=1.4*duration.
peduration = duration*1.4   #Activity duration follows beta(a, b, 3- , 3+ ), a=0.8*duration, b=1.4*duration.
succ = [[1,2,3],[4,9,10],[6,12,17],[5,8,15],[14],[7,11,16],[21],[13],[21],[13,28,30],[20],[29],[15,24],[24],[18],[19,25],[22],[21],[20,22],[23],[27],[24,28],[29],[27,30],[25],[26],[27],[29],[31],[31],[31],[]]

def riskanalysis():
	
	
	return ci, cri #return the Criticality Index and Cruciality Index of each activity

if __name__ == "__main__":
	ci, cri = riskanalysis()