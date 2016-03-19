def MediaReal(vetor):
    media = 0

    for i in range(len(vetor)):
        media += vetor[i]
                       
    return media/len(vetor)

def MedianaReal(vetor):
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
    
def AmplitudeTotalReal(vetor):
    lista = []
    for i in range(len(vetor)):
        lista.append(vetor[i])
    lista.sort()
    AmpTotal = vetor[len(vetor)-1] - vetor[0]    
    
    return AmpTotal

def VarianciaReal(vetor):
	Desvio=0
	for i in range(len(vetor)):
		Desvio = Desvio+((vetor[i]-MediaReal(vetor))*(vetor[i]-MediaReal(vetor)))
	Variancia=Desvio/len(vetor)
	return Variancia

def DesvioPadraoReal(vetor):
    
    DesvioPadrao = VarianciaReal(vetor)**(1.0/2.0)
    
    return DesvioPadrao

def CoefVariacaoReal(vetor):
    
    CoefVariacao = DesvioPadraoReal(vetor)/MediaReal(vetor)
    
    return CoefVariacao

def CovarianciaReal(vetor, vetorI):
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

def CoefCorrelacaoReal(vetor, vetorI):
    
    CoefCorrelacao = CovarianciaReal(vetor, vetorI)/(DesvioPadraoReal(vetor)*DesvioPadraoReal(vetorI))
    
    return CoefCorrelacao

