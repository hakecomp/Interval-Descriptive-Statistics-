#\QualitativeMetrics.py
#
# Copyright 2018 Aline Brum Loreto<aline.loreto@lower.ufpel.edu.br>, Alice Fonseca Finger <aliceffinger@gmail.com>, Mauricio Dorneles
# Caldeira Balboni<mdcbalboni@lower.ufpel.edu.br>,Lucas Mendes Tortelli <lmtortelli@lower.ufpel.edu.br>, Vinicius Signori Furlan<vsfurlan@.lower.ufpel.edu.br>
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

__all__ = ["QualitativeMetrics"]

class QualitativeMetrics(object):

    @staticmethod
    def relativeError(xInt,xReal):
        '''
        Relative Error metric operation.
        See more details in: 
        [4] Loreto, A.B., Analise de Complexidade Computacional de Problemas de Estatistica Descritiva com Entradas Intervalares,
        Tese de Doutorado em PPGC, UFRGS, Porto Alegre, 2006.
        
        The first value represents the result and the second the error
        Some example:
        
        >>> relativeError(IReal(0.5,2.0),1.0)
        (0.25, 1.5)
        
        '''
        try:
            r = abs((xReal - QualitativeMetrics.centeri(xInt))/xReal)
            error = (QualitativeMetrics.diameter(xInt))/(2*xInt.inf)
        except:
            r = "NaN"
            error = "NaN"
        return r,error

    @staticmethod
    def diameter(xInt):
        '''
        Diameter operation like qualitative metric
        
        Some example:

        >>> from intpy import *
        >>> from intStatistics import *
        >>> from intStatistics.error import *
        >>> diameter(IReal(0.25,1.75))
        1.5  
        '''
        return xInt.sup - xInt.inf

    @staticmethod
    def centeri(xInt):
        '''
        Indicates the center of interval

        Some example:
        
        >>> x = IReal(5.67,9.65)
        >>> centeri(x)
        7.66
        '''
        return (xInt.inf + xInt.sup)/2.0

    @staticmethod
    def absoluteError(xInt,xReal):
        '''
        Absolute Error metric operation.
        See more details in: 
        [4] Loreto, A.B., Analise de Complexidade Computacional de Problemas de Estatistica Descritiva com Entradas Intervalares,
        Tese de Doutorado em PPGC, UFRGS, Porto Alegre, 2006.
        
        The first value represents the result and the second the error
        Some example:
        
        >>> absoluteError(IReal(0.5,2.0),1.0)
        (0.25, 0.75)
        
        '''
        try:
            r = abs((xReal - QualitativeMetrics.centeri(xInt))/xReal)
            error = (QualitativeMetrics.diameter(xInt)/2.0)
        except:
            r = "NaN"
            error = "NaN"
        return r,error
