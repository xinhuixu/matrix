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
    for r in range(len(matrix)):
        matrix[r][r] = 1

def scalar_mult( matrix, s ):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            matrix[r][c] = matrix[r][c] * s 

def scalar_add( matrix, s ):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            matrix[r][c] = matrix[r][c] + s 

def copy( src ):
    new = new_matrix(4, len(src[0]))
    for r in range(4):
        for c in range(len(src[0])):
            new[r][c] = src[r][c]
    return new

#m1 * m2 -> m2
#we will always have a (4x4)(4xN) = (4xN) matrix...
#NEED TO MODIFY M2
def matrix_mult( m1, m2 ):
    len_m2c = len(m2[0])
    m2temp = copy( m2 )
    for r in range(4):
        for c in range(len_m2c):
            cell = 0
            for c1 in range(4):
                
                cell += m1[r][c1] * m2temp[c1][c]
                #print "INSIDE cell: ", cell
            #print "cell: ", cell
            m2[r][c] = int(cell)
        

#default rows = 4        
def new_matrix(rows, cols):
    m = []
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[r].append( 0 )
    return m


