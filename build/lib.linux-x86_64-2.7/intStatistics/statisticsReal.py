# Copyright 2015 Aline Brum Loreto<aline.loreto@inf.ufpel.edu.br>, Alice Fonseca Finger <aliceffinger@gmail.com>, Mauricio Dorneles
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

def average(vetor):
    media = 0

    for i in range(len(vetor)):
        media += vetor[i]

    return media/len(vetor)

def median(vetor):
    lista = []
    for i in range(len(vetor)):
        lista.append(vetor[i])
    lista.sort()
    metade=len(vetor)/2
    if((len(vetor)%2) == 0):
        mediana = (vetor[metade]+vetor[metade-1])/2
    else:
        mediana = vetor[metade]
    return mediana

def ranges(vetor):
    lista = []
    for i in range(len(vetor)):
        lista.append(vetor[i])
    lista.sort()
    AmpTotal = vetor[len(vetor)-1] - vetor[0]

    return AmpTotal

def variance(vetor):
	desvi=0
	for i in range(len(vetor)):
		desvi = desvi+((vetor[i]-average(vetor))*(vetor[i]-average(vetor)))
	variance=desvi/len(vetor)
	return variance

def deviance(vetor):

    DesvioPadrao = variance(vetor)**(1.0/2.0)

    return DesvioPadrao

def coefVariance(vetor):
    CoefVariacao = deviance(vetor)/average(vetor)
    return CoefVariacao

def coVariance(vetor, vetorI):
    sumX = 0.0
    sumY = 0.0
    prodXY = 0.0
    n = 0
    sumXY = 0.0
    if(len(vetor) <= len(vetorI)):
        n = len(vetor)
    else:
        n = len(vetorI)

    for i in range(n):
        prodXY+= vetor[i]*vetorI[i]
        sumX+=vetor[i]
        sumY+=vetorI[i]

    sumXY = (sumX*sumY)/n
    Covariancia = (prodXY - sumXY)/n
    return Covariancia

def coefCorrelation(vetor, vetorI):
    CoefCorrelacao = coVariance(vetor, vetorI)/(deviance(vetor)*deviance(vetorI))
    return CoefCorrelacao
