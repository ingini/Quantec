##########numba 버전############

from math import cos, log
def f_py(I, J):
    res = 0
    for i in range(I):
        for j in range (J):
            res += int(cos(log(1)))
    return res

I, J = 2500, 2500
%time f_py(I, J)

def f_np(I, J):
    a = np.ones((I, J), dtype=np.float64)
    return int(np.sum(np.cos(np.log(a)))), a


%time res, a = f_np(I, J)

import numba as nb

f_nb = nb.jit(f_py)

%time f_nb(I, J)

#############cython############

def f_py(I, J):
    res = 0.  # we work on a float object
    for i in range(I):
        for j in range (J * I):
            res += 1
    return res

I, J = 500, 500
%time f_py(I, J)

import pyximport
pyximport.install()

%load_ext Cython

%%cython
#
# Nested loop example with Cython
#
def f_cy(int I, int J):
    cdef double res = 0
    # double float much slower than int or long
    for i in range(I):
        for j in range (J * I):
            res += 1
    return res


%time res = f_cy(I, J)