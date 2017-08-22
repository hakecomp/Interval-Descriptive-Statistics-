# setup.py
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


from distutils.core import Extension
from distutils.core import setup


_package_description = """Interval Statistics Package

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
[4] Loreto, A.B., Analise de Complexidade Computacional de Problemas de Estatistica Descritiva com Entradas Intervalares,
	Tese de Doutorado em PPGC, UFRGS, Porto Alegre, 2006.
[5] Ratschek, H., Rokne,J., New Computer Methods for Global Optimization., Ellis Horkwood, 1988.


It was developed in TEIa/UFPel (Brazil) by Aline Brum Loreto, Alice Fonseca Finger, Lucas Mendes Tortelli, Mauricio Dorneles Caldeira Balboni and Vinicius Signori Furlan
<lmtortelli@inf.ufpel.edu.br, lmtortelli@hotmail.com> and it's free software.
""".split("\n")


if __name__ == "__main__":
    setup(
        name="intStatistics",
        version="0.1.7",
        description=_package_description[0],
        long_description="\n".join(_package_description[2:-1]),
        author="Aline Brum Loreto, Alice Fonseca Finger, Lucas Mendes Tortelli, Mauricio Dorneles Caldeira Balboni, Vinicius Signori Furlan",
        author_email="aline.loreto@gmail.com, aliceffinger@gmail.com,lmtortelli@inf.ufpel.edu.br,mdcbalboni@inf.ufpel.edu.br,vsfurlan@inf.ufpel.edu.br",
        license="GPL",
        platforms=[
            "Windows",
            "Linux"
        ],
        packages=[
            "intStatistics",
        ],
        package_dir={
            "intStatistics" : "src"
        },
        requires=[
            "fpconst",
            "intPy"
        ]


    )
