from __future__ import division
import math


def print_matrix( matrix ):
    mat = "["
    for row in matrix:
        for col in row:
            mat += str(col) + " "
        mat += "\n"
    mat = mat[:-2]
    mat += "]"
    print mat

def ident( matrix ):
    pass

def scalar_mult( matrix, s ):
    ret = new_matrix(4, len(matrix[0])) #4xN
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            ret[r][c] = matrix[r][c] * s 
    return ret


#m1 * m2 -> m2
#we will always have a (4x4)(4xN) = (4xN) matrix...
def matrix_mult( m1, m2 ):
    ret = new_matrix(4, len(m2[0]))
    for r in range(len(m2)):
        cell = 0        
        for c in range(len(m2[r])):
            cell += m1[r][c] * m2[c][r]
            ret[r][c] = cell
    return ret

#default rows = 4        
def new_matrix(rows, cols):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

#TEST
M = new_matrix(4, 4)
#print_matrix(M)
M = scalar_mult(M,5)
print "M"
print_matrix(M)

N = new_matrix(4, 4)
print "N"
print_matrix(N)
'''
N = matrix_mult(M, N)
print "NxM"
print_matrix(N)
'''
