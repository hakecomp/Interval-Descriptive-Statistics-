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

from intpy import *
from math import sqrt

#Initiate a list of interval values. The parameters are a list of real values and a precision.
def initInterval(vetor,delta):
    vetorI = list();
    for i in range(len(vetor)):
        vetorI.append(IReal(vetor[i]) + IReal(-delta,delta))
    return vetorI
# Interval SQRT
def sqrtI(dado):
    result = IReal(sqrt(dado.inf), sqrt(dado.sup))
    
    return result

# Performs exponentiation operation interval
def powI(dado, exp):
    result = IReal(dado.inf**exp, dado.sup**exp)
    
    return result
    
