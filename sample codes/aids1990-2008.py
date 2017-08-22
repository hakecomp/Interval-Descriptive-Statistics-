from sys import *

import time
from intStatistics import *
from math import sqrt

RS = [5.0,12.0,7.0,47.0,7.0,79.0,10.0,59.0,12.0,46.0,14.0,42.0,17.0,55.0,21.0,78.0,28.0,62.0,24.0]
SP = [16.0,68.0,21.0,27.0,25.0,97.0,27.0,48.0,28.0,19.0,31.0,53.0,34.0,1.0,34.0,13.0,36.0,77.0,31.0]

incidenciasAIDSRS = initInterval(RS,0.00000000001)
incidenciasAIDSSP = initInterval(SP,0.00000000001)


print "Media:",average(RS)
print "Mediana:",median(RS)
print "Amplitude:",ranges(RS)
print "Variancia:",variance(RS)
print "Desvio Padrao:",deviance(RS)
print "Covariancia:",coVariance(RS,SP)
print "Coeficiente de Correlacao:",coefCorrelation(RS,SP)
print "Coeficiente de Variacao:",coVariance(RS,SP)

print ""
print "Media:",iAverage(incidenciasAIDSRS)
print "Mediana:",iMedian(incidenciasAIDSRS)
print "Amplitude:",iRange(incidenciasAIDSRS)
print "Variancia:",iVariance(incidenciasAIDSRS)
print "Desvio Padrao:",iSDeviation(incidenciasAIDSRS)
print "Covariancia:",icoVariance(incidenciasAIDSRS,incidenciasAIDSSP)
print "Coeficiente de Correlacao:",icoefCorrelation(incidenciasAIDSRS,incidenciasAIDSSP)
print "Coeficiente de Variacao:",icoefVariance(incidenciasAIDSRS)
