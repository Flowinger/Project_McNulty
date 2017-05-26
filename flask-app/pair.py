import numpy as numpy
import pandas as pd

#you are given two sorted lists, of length m and n. 
#Write a function that will merge the two lists into a single sorted list.

a = [1,3,5,6]
b = [2,4,7] 
#Output [1,2,3,4,5,6,7]
#Input [15] [12] Output [12,15]
#Input [] [1,2] Output [1,2]
#Extra Credit Make this run faster. you should be able to do this in m+n-1 operations.
#Make this work on k sorted lists

def mergelists(l1,l2):
	merged = []
	one = 0
	two = 0
	while two < len(l2) and one < len(l1):
		if l1[one] >= l2[two]:
			merged.append(l2[two])
			two += 1
		else:
			merged.append(l1[one])
			one += 1
	if  one == len(l1):
		merged.extend(l2[two:])
	else:
		merged.extend(l1[one:])
	return merged
print(mergelists(a,b))