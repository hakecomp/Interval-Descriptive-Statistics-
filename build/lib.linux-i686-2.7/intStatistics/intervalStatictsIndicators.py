from intpy import *
from intpy.support.stdfunc import sqrt
from sys import *
from initIntervals import *


#Execute mean on list of interval values
def iMean(intervalList):
		mean = IReal(0)
		for i in range(len(intervalList)):
			mean += intervalList[i]/(len(intervalList))
		
		return mean


#Execute the Median of list interval values
def iMedian(intervalList):
	lowers = []
	uppers = []
	for i in range(len(intervalList)):
		lowers.append(intervalList[i].inf)
		uppers.append(intervalList[i].sup)
	
	lowers.sort()
	uppers.sort()
	
	half=len(intervalList)/2
	
	if((len(intervalList)%2) == 0):
		lower = (lowers[half] + lowers[half-1])/2
		upper = (uppers[half] + uppers[half-1])/2
		mean = IReal(lower,upper)
	
	else:
		lower = lowers[half]
		upper = uppers[half]
		mean = IReal(lower,upper)    
	return mean
    
# COMENT ABOUT THIS FUNCTION
def iRange(intervalList):
	AmpTotal = IReal(0)
	lowers = []
	uppers = []
	
	for i in range(len(intervalList)):
		lowers.append(0)
		uppers.append(0)
		lowers[i] = intervalList[i].inf
		uppers[i] = intervalList[i].sup
	
	lowers.sort()
	uppers.sort()
	if(intervalList[len(intervalList)-1].inf > intervalList[0].sup):
		upper = uppers[len(uppers)-1] - uppers[0]
		lower = lowers[len(lowers)-1] - lowers[0]
		AmpTotal = IReal(lower,upper)
	else:
		upper = lower[len(intervalList)-1] - lower[0]
		AmpTotal = IReal(0, upper)
        
	return AmpTotal


#COMENT ABOUT THIS FUNCTION
def iVariance(intervalList):
    variance = IReal(0)
    variance = IReal(0)
    for i in range(len(intervalList)):
        variance += (powI((intervalList[i] - iMean(intervalList)), 2))
    variance = variance/len(intervalList)
    return variance

#COMENT ABOUT THIS FUNCTION
def iSDeviation(intervalList):
    
    standardDeviation = sqrtI(iVariance(intervalList))
    return standardDeviation


#COMENT ABOUT THIS FUNCTION
def icoefVariance(intervalList):
    
    coefVariance = iSDeviation(intervalList)/iMean(intervalList)
    return coefVariance

# COMENT ABOUT THIS FUNCTION
#BEM DEFINIDA?
def icoVariance(intervalListOne, intervalListTwo):
    coVariance = IReal(0.0);
    meanX = iMean(intervalListOne)
    meanY = iMean(intervalListTwo)
    a = []
    
    if((len(intervalListOne)) <= (len(intervalListTwo))):
        n = len(intervalListOne)
    
    else:
        n = len(intervalListTwo)
    
    for i in range(n):
    	productXinf = intervalListOne[i].inf - meanX.sup
    	productXsup = intervalListOne[i].sup - meanX.inf
    	productYinf = intervalListTwo[i].inf - meanY.sup
    	productYsup = intervalListTwo[i].sup - meanY.inf
    	X = IReal(productXinf,productXsup)
    	Y = IReal(productYinf,productYsup)
        coVariance+=IReal(X.inf*Y.inf,X.sup*Y.sup)
       	
    return coVariance/(n)

# COMENT ABOUT THIS FUNCTION

def icoefCorrelation(intervalListOne, intervalListTwo):
    
    coefCorrelation = icoVariance(intervalListOne, intervalListTwo)/(iSDeviation(intervalListOne)*iSDeviation(intervalListTwo))
    return coefCorrelation

