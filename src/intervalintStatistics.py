# Copyright 2017 Aline Brum Loreto<aline.loreto@inf.ufpel.edu.br>, Alice Fonseca Finger <aliceffinger@gmail.com>, Mauricio Dorneles
# Caldeira Balboni<mdcbalboni@inf.ufpel.edu.br>,Lucas Mendes Tortelli <lmtortelli@inf.ufpel.edu.br>, Vinicius Signori Furlan<vsfurlan@.inf.ufpel.edu.br>
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from intpy import *
from intpy.support.stdfunc import sqrt
from sys import *
from initInterval import *


#This method is responsible for performing averaging operation on the received list of interval values.
def iAverage(intervalList):
		averageResult = IReal(0)
		for i in range(len(intervalList)):
			averageResult += intervalList[i]/(len(intervalList))

		return averageResult


#It uses the default sort operation of Python on the lists of the lower and upper limits . After performing the median.
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
		Average = IReal(lower,upper)

	else:
		lower = lowers[half]
		upper = uppers[half]
		Average = IReal(lower,upper)
	return Average

# Realization of the full range of operation on the list of received interval values.
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


#The variance of operation is used the average operation of that package, getting a list of inervalares values.
def iVariance(intervalList):
    variance = IReal(0)
    variance = IReal(0)
    for i in range(len(intervalList)):
        variance += (powI((intervalList[i] - iAverage(intervalList)), 2))
    variance = variance/len(intervalList)
    return variance

# The standard deviation contains dependence of the variance,
# applied to the interval data list received to perform the calculation.
def iSDeviation(intervalList):

    standardDeviation = sqrtI(iVariance(intervalList))
    return standardDeviation


#The coefficient of variation performs the operation that holds your name,
#depending on the mean and standard deviation of operationN
def icoefVariance(intervalList):

    coefVariance = iSDeviation(intervalList)/iAverage(intervalList)
    return coefVariance

# This method has dependence of the average operation to correct performance of its calculation
# But this operation is applied to two lists of interval values each belonging to people who want to Benchmark
def icoVariance(intervalListOne, intervalListTwo):
    coVariance = IReal(0.0);
    AverageX = iAverage(intervalListOne)
    AverageY = iAverage(intervalListTwo)
    a = []

    if((len(intervalListOne)) <= (len(intervalListTwo))):
        n = len(intervalListOne)

    else:
        n = len(intervalListTwo)

    for i in range(n):
    	productXinf = intervalListOne[i].inf - AverageX.sup
    	productXsup = intervalListOne[i].sup - AverageX.inf
    	productYinf = intervalListTwo[i].inf - AverageY.sup
    	productYsup = intervalListTwo[i].sup - AverageY.inf
    	X = IReal(productXinf,productXsup)
    	Y = IReal(productYinf,productYsup)
        coVariance+=IReal(X.inf*Y.inf,X.sup*Y.sup)

    return coVariance/(n)

# Method contains dependence of the correlation coefficient used when needed to determine the correlation between two sets of data

def icoefCorrelation(intervalListOne, intervalListTwo):

    coefCorrelation = icoVariance(intervalListOne, intervalListTwo)/(iSDeviation(intervalListOne)*iSDeviation(intervalListTwo))
    return coefCorrelation
