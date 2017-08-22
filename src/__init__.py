# __init__.py
#
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
# MA 02110-1301, USA.


"""Interval Statistics Package

This package provides statistics methods for Maximum Accuracy Interval Arithmetic.

The Interval Arithmetic is a mathematical tool for the solution of problems
related to numerical errors, based on an algebraic system formed by all closed
intervals of Real Line (or rectangles of Complex Plane) and operations defined
on it. Rather than usual numerical algorithms, it's used interval algorithms
producing intervals containing the correct answer as a result.

The Maximum Accuracy, on the other hand, provides an axiomatic method for
arithmetic operations performed in computers that capture essential properties
associated with rounding.

The studies on large amounts of data , one needs to descriptive statistics in order to
reduce the complexity of analyzing all the data.
But these acquired data must be reliable and accurate .
Thus joins use of the advantages of using descriptive statistics with the benefits provided by interval arithmetic .
Thus this package have as objectives to provide methods for calculation of descriptive indicators
 to provide an automatic control errors and maximum accuracy.

For more information about it, see:

[1] Moore, R. E., Interval Analysis. Prentice-Hall, Englewood Cliffs, New
    Jersey, 1966.
[2] Moore, R. E., Methods and Applications of Interval Analysis. SIAM Studies
    in Applied Mathematics, Philadelphia, 1979.
[3] Kulisch, U. W., Miranker, W. L., Computer Arithmetic in Theory and
    Practice. Academic Press, 1981.
[4] Loreto, A.B., An´alise de Complexidade Computacional de Problemas de Estat´istica Descritiva com Entradas Intervalares"
    Tese de Doutorado em PPGC, Instituto de Informatica / UFRGS, Porto Alegre, 2006.
[5] Ratschek, H., Rokne,J., "New Computer Methods for Global Optimization.", Ellis Horkwood, 1988.


It was developed in TEIa/UFPel (Brazil) by Aline Brum Loreto, Alice Fonseca Finger, Lucas Mendes Tortelli, Mauricio Dorneles Caldeira Balboni and Vinicius Signori Furlan
<lmtortelli@inf.ufpel.edu.br, lmtortelli@hotmail.com> and it's free software.
"""

from intStatistics.intervalintStatistics import *
from intStatistics.initInterval import *
from intStatistics.statisticsReal import *

def _test():
    from doctest import DocTestSuite
    from inspect import getmodule
    from os import walk
    from os.path import abspath, dirname, join
    from unittest import TestSuite, TextTestRunner
    test_suite = TestSuite()
    for root, dirs, files in walk(dirname(abspath(__file__))):
        module_files = [join(root, file) for file in files if \
            file.endswith(".py")]
        test_suite.addTests(DocTestSuite(getmodule(None, file)) for file in \
            module_files)
    TextTestRunner().run(test_suite)


if __name__ == "__main__":
    _test()
