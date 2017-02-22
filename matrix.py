import math

def print_matrix( matrix ):
    mat = ""
    for row in matrix:
        for col in row:
            mat += str(col) + " "
        mat += "\n"
    mat = mat[:-1]
    print mat

def ident( matrix ):
    pass

def scalar_mult( matrix, s ):
    pass

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

#TEST
M = new_matrix()
print_matrix(M)
